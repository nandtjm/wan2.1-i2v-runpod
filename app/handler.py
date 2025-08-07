import runpod
import logging
from model_loader import pipeline

# Configure logging
logging.basicConfig(level=logging.INFO)

def generate_output(job):
    job_input = job.get("input", {})
    image_1 = job_input.get("image1")
    image_2 = job_input.get("image2")

    if not image_1 or not image_2:
        return {"error": "Missing input images."}

    try:
        result_path = pipeline(image_1, image_2)
        return {"output": result_path}
    except Exception as e:
        logging.exception("Error generating output:")
        return {"error": str(e)}

runpod.serverless.start({"handler": generate_output})
