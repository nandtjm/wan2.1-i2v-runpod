# WAN2.1 I2V RunPod Serverless Endpoint

This repository allows you to deploy a serverless endpoint on RunPod to generate short romantic animation clips using two images as input.

## 🔧 Model Setup (RunPod Storage)

Mount your persistent storage to `/runpod-volume/`:

- Base Model: `/runpod-volume/models/Wan2.1-I2V-14B-720P/`
- LoRA Weights: `/runpod-volume/models/kissing-lora/`

## 🛠️ Build & Deploy

```bash
git clone https://github.com/your-user/wan2.1-i2v-runpod.git
cd wan2.1-i2v-runpod

# Zip for RunPod Serverless upload
zip -r wan2.1-i2v.zip .
