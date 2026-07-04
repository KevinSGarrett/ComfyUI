# Self-Hosted LLM Policy

This policy applies to:

- `C:\Comfy_UI_Lora\AI_LLM_Intelligence_Plan`
- `C:\Comfy_UI_Lora\AI_Front`
- Any AI assistant, prompt helper, reviewer, planner, router, UI copilot, or automation layer added to the ComfyUI/Wave42 system.

## Default Architecture

Use a self-hosted LLM by default.

Preferred order:

1. Local machine LLM endpoint when the local computer can run it reliably.
2. EC2-hosted LLM endpoint when GPU/server capacity is needed.
3. External provider fallback only when self-hosting is technically blocked or a specific provider feature is truly required.

The AI front end and intelligence layers should talk to an OpenAI-compatible local endpoint where possible so the backend can switch between engines without rewriting the app.

Recommended environment contract:

```powershell
$env:WAVE42_LLM_PROVIDER = "self_hosted"
$env:WAVE42_LLM_BASE_URL = "http://127.0.0.1:11434/v1"
$env:WAVE42_LLM_MODEL = "local-model-name"
$env:WAVE42_LLM_API_KEY = "not-required-for-local-or-use-local-placeholder"
```

Alternative local endpoints may include:

- Ollama OpenAI-compatible endpoint.
- llama.cpp or llama-cpp-python server.
- LM Studio local server.
- text-generation-webui OpenAI-compatible API.
- vLLM on EC2 or local Linux.

## EC2 Hosting

If the LLM runs on EC2, Lane 4 owns runtime start/stop, endpoint reachability, and cost control. Do not expose an unauthenticated public LLM endpoint.

Prefer:

- SSM port forwarding.
- SSH tunnel.
- Private security group access.
- Short live windows for model tests.

Record:

- model name
- model family
- quantization
- path
- SHA256 or source manifest
- runtime host
- endpoint URL shape without credentials
- load result
- latency/basic health check
- cost state before/after

## External Provider Fallbacks

OpenAI, Grok, Anthropic, or other cloud providers are not the default. They may be used only when:

- self-hosted LLM is blocked by hardware, missing model, quality, or runtime constraints;
- a required capability cannot reasonably be reproduced locally;
- credentials and provider terms permit the task;
- no secrets are printed or committed;
- the fallback is recorded as a fallback, not as the primary production architecture.

Do not send private project files, prompts, media metadata, tracker content, credentials, or unreleased evidence to an external provider unless the user explicitly approves that route.

## Lane Ownership

- Lane 3 owns local/EC2 LLM model inventory, download/acquisition evidence, compatibility, quantization, and load testing.
- Lane 4 owns EC2 LLM runtime hosting, endpoint checks, tunnels, and stop-state proof.
- Lane 5 owns QA of LLM-generated decisions, evidence mapping, and tracker claims.
- Lane 6 owns AI front-end integration, prompt/preset assistant behavior, and generated candidate/preset workflows.

## Minimum Evidence

A self-hosted LLM integration is not proven until evidence shows:

- endpoint is reachable;
- model identity is known;
- no external provider is required for the normal path;
- sample request and response work without leaking secrets;
- latency and failure behavior are recorded;
- AI output is treated as advisory unless downstream QA/evidence confirms it.

