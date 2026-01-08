import os
from pathlib import Path
from transformers import HfArgumentParser

from ltx_video.inference import infer, InferenceConfig


def run_live_test():
    """
    Minimal live test to confirm:
    - inference runs
    - video is written to disk
    """
    os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

    config = InferenceConfig(
        prompt="A cinematic shot of a futuristic city at sunset",
        # conditioning_media_paths=["assets/example.png"],
        conditioning_start_frames=[0],
        height=384,
        width=640,
        num_frames=20,
        pipeline_config="configs/ltxv-2b-0.9.8-distilled-3060-12gb.yaml",
        seed=42,
        output_path="outputs",
    )

    # 🔑 FORCE saving
    config.save_video = True

    # Ensure output dir exists
    Path(config.output_path).mkdir(parents=True, exist_ok=True)

    print("=== LTX LIVE TEST ===")
    print("SAVE VIDEO :", config.save_video)
    print("OUTPUT PATH:", Path(config.output_path).resolve())
    print("====================")

    infer(config=config)

    print("=== INFERENCE FINISHED ===")
    print("Check outputs/ for generated .mp4 files")


def main():
    """
    Normal CLI entrypoint (unchanged behavior)
    """
    parser = HfArgumentParser(InferenceConfig)
    config = parser.parse_args_into_dataclasses()[0]

    config.output_path = "outputs"
    config.save_video = True

    Path(config.output_path).mkdir(parents=True, exist_ok=True)

    infer(config=config)

    print("SAVE VIDEO:", config.save_video)
    print("OUTPUT PATH:", Path(config.output_path).resolve())


if __name__ == "__main__":
    # 🔥 COMMENT / UNCOMMENT what you want to test

    run_live_test()  # ← use this to test immediately
    # main()            # ← use this when calling from run_offline.bat
