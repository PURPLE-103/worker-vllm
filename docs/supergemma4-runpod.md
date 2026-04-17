# SuperGemma4 Runpod Notes

Target model:

```text
Jiunsong/supergemma4-26b-abliterated-multimodal
```

The model ships its own `chat_template` in `tokenizer_config.json`, so do not set
`CHAT_TEMPLATE` for this model. The worker will use the bundled template from the
cached Hugging Face snapshot.

Recommended Runpod environment:

```text
MODEL_NAME=Jiunsong/supergemma4-26b-abliterated-multimodal
OPENAI_SERVED_MODEL_NAME_OVERRIDE=supergemma4-26b-abliterated-multimodal

MAX_MODEL_LEN=32768
MAX_NUM_BATCHED_TOKENS=32768
MAX_NUM_SEQS=1
GPU_MEMORY_UTILIZATION=0.95

ENABLE_AUTO_TOOL_CHOICE=true
TOOL_CALL_PARSER=gemma4
REASONING_PARSER=gemma4
LIMIT_MM_PER_PROMPT=image=1
```

If `MAX_MODEL_LEN`, `MAX_NUM_BATCHED_TOKENS`, and `MAX_NUM_SEQS` are not set,
the worker applies the same 32k/single-sequence defaults for this model.

Context length is mainly a memory constraint. Higher context increases KV cache
memory roughly linearly, and the model config advertises a very large 262k
maximum. On an A100 80GB, trying to allocate near that maximum is expected to
fail with OOM. Longer prompts are also slower, but for this deployment the first
hard limit is VRAM, not throughput.

To experiment upward, raise both `MAX_MODEL_LEN` and `MAX_NUM_BATCHED_TOKENS`
together, for example 49152 or 65536, and keep `MAX_NUM_SEQS=1`.
