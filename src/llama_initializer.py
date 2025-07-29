from llama_cpp import Llama

def load_llama_model(model_path: str, context_length: int = 1024):
    return Llama(
        model_path=model_path,
        n_ctx=context_length,
        verbose=False
    )
