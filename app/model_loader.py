import os
import logging
from diffusers import AnimateDiffPipeline, LCMScheduler, MotionAdapter

MODEL_DIR = "/runpod-volume/models/Wan2.1-I2V-14B-720P"
LORA_DIR = "/runpod-volume/models/kissing-lora"

logging.info(f"Loading base model from {MODEL_DIR}")
pipeline = AnimateDiffPipeline.from_pretrained(
    MODEL_DIR,
    motion_adapter=MotionAdapter(),
    torch_dtype="auto"
)

logging.info(f"Loading LoRA from {LORA_DIR}")
pipeline.load_lora_weights(LORA_DIR)

pipeline.scheduler = LCMScheduler.from_config(pipeline.scheduler.config)
pipeline.enable_model_cpu_offload()
pipeline.enable_vae_slicing()
pipeline.to("cuda")

def pipeline(image_1: str, image_2: str) -> str:
    prompt = "romantic cinematic kissing moment, anime style, dramatic lighting, close-up, ultra detailed"
    result = pipeline(prompt=prompt, image1=image_1, image2=image_2).images[0]
    
    output_path = "/tmp/generated_kissing.png"
    result.save(output_path)
    return output_path
