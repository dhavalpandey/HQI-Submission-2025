# Quantum Shorts: Visualizing Shor's Algorithm

This project is a submission for the **HQI Shorts Competition**, visually explaining **Shor's Algorithm** and its implications for quantum cryptography threats. The animations are created using **Manim**, a Python library for mathematical animations.

## Project Structure

-   **`drafts/`**: Contains draft versions of the animation scripts.
    -   `draft1.py`, `draft2.py`, `draft3.py`: Iterative drafts of the animation code.
-   **`media/videos/`**: Contains the final rendered video submission.

    -   `video/`: Directory for the final video and related assets.

-   **`video.py`**: The final Manim script used to generate the animation.

## Description

The animation provides a step-by-step visual explanation of:

1. **Shor's Algorithm**: A quantum algorithm for integer factorization.
2. **Quantum Cryptography Threats**: How quantum computing could break classical encryption methods like RSA.

The video uses engaging visuals, including:

-   Historical context (Turing, RSA, Shor).
-   Superposition and quantum states.
-   Period finding and wave interference (QFT).
-   A call to action for exploring quantum computing.

## How to Run

1. Install **Manim**: Follow the [Manim installation guide](https://docs.manim.community/en/stable/installation.html).
2. Run the final script:
    ```bash
    manim -pql video.py QuantumEncryptionVideoEnhanced
    ```
