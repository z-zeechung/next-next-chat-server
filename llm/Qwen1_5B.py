from typing import Generator, List, Literal

from data_types import Message, Tool
from llm.LLM import LLM


class Qwen1_5B(LLM):
    def __init__(self):
        from transformers import AutoModelForCausalLM, AutoTokenizer

        model_name = "Qwen/Qwen2.5-1.5B-Instruct"

        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype="auto",
            device_map="auto",
            cache_dir='.cache'
        )
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir='.cache')

    def chat(self, messages: List[Message], model: Literal['regular', 'smart', 'long'], tools: List[Tool]) \
         -> Generator[str, None, None]:
        
        import torch

        messages = [{"role": m.role, "content": m.content} for m in messages]
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)
        
        # 设置流式生成的参数
        output_chunk_size = 1  # 每次生成的词元数量
        max_new_tokens = 512  # 总共要生成的词元数量上限
        current_num_tokens = 0  # 当前已生成的词元数量

        result = ""
        
        # 开始流式生成
        with torch.no_grad():
            while current_num_tokens < max_new_tokens:
                outputs = self.model.generate(
                    **model_inputs,
                    max_length=model_inputs.input_ids.shape[-1] + output_chunk_size,
                    num_return_sequences=1,
                    pad_token_id=self.tokenizer.eos_token_id,  # 通常设置为EOS token，以便在生成完成时停止
                    eos_token_id=self.tokenizer.eos_token_id,  # EOS token用于标识生成的结束
                )
                
                # 获取新生成的词元（忽略已经生成的部分）
                new_tokens = outputs[:, model_inputs.input_ids.shape[-1]:]
                if new_tokens.shape[-1] == 0:  # 如果没有新生成的词元，则退出循环
                    break

                if new_tokens[0].item()==198:
                    break
                
                # 解码新生成的词元并产出（yield）它们
                decoded_tokens = self.tokenizer.decode(new_tokens[0], skip_special_tokens=True)
                result += decoded_tokens
                yield result  # 这里可能需要根据实际情况调整，以确保按词元或适当的文本块产出
                
                # 更新输入以包含新生成的词元，为下一轮生成做准备
                model_inputs = self.tokenizer.encode_plus(
                    self.tokenizer.decode(outputs[0]),
                    return_tensors="pt",
                    add_special_tokens=False,
                ).to(self.model.device)
                
                # 更新已生成的词元数量
                current_num_tokens += new_tokens.shape[-1]