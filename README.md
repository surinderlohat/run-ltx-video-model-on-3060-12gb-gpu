## This is the working configuration for SYSTEM with 

If you reach here Don't forgot to mark STAR this repo to ge new updates 

SYSTEM CONFIG
```
3060 12GB  GPU
i5 9400f CPU 
24 GB DDR4 RAM
```

So if you have this configuration or > then this then you are good to go

We are using the 2b model it gives me a good result for my use case genration of the 5-10 sec videos

Follow these steps: https://github.com/Lightricks/LTX-Video


1. Now use update inference.py  with code from this current repo i have added some tweaks to make testing easy.
2. User the configurations folder copy config ltxv-2b-0.9.8-distilled-3060-12gb.yaml
3. the tun inference.py

```
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
```

Output FROM My 3060 12GB GPU

https://github.com/user-attachments/assets/1cc5dc0f-870e-4fe7-b3e3-a08ed5d4da28


---
Prompt
```
A peaceful Indian village at sunrise, soft toon animation style, warm pastel colors. Mud houses with tiled roofs, narrow village path, trees gently moving in the breeze. A young boy walks calmly through the village. Calm, emotional storytelling mood. Clean line art, consistent outlines, sharp edges, high quality animation, no blur, no softness, stable lighting, professional cartoon rendering.
```

Output:


https://github.com/user-attachments/assets/90442bbf-86cb-4656-8832-c4a63cab3932





