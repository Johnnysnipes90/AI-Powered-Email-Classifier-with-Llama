from llama_cpp import Llama

def load_llama_model(path_to_model, ctx=512, threads=4):
    return Llama(model_path=path_to_model, n_ctx=ctx, n_threads=threads)