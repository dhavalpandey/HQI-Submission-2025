from manim import *
import random

# --- Configuration for a 3Blue1Brown-style appearance ---
DARK_BACKGROUND_COLOR = "#090d1a" # Very dark blue-grey
TEXT_COLOR = WHITE
PRIMARY_ACCENT_COLOR = "#FFD700"  # Gold/Yellow
SECONDARY_ACCENT_COLOR = "#38a3a5" # Teal/Blue
ERROR_COLOR = "#FF3333" # Red for "nope"
GRAPH_COLOR = GREEN_C   # A bright green for graphs

class QuantumEncryptionVideo(Scene):
    def construct(self):
        self.camera.background_color = DARK_BACKGROUND_COLOR

        # Helper for consistent text positioning and styling (optional)
        def create_main_title(text_content):
            return Text(text_content, font_size=60, color=TEXT_COLOR, weight=BOLD)

        def create_subtitle(text_content):
            return Text(text_content, font_size=32, color=PRIMARY_ACCENT_COLOR)

        def create_caption(text_content, color=TEXT_COLOR):
            return Text(text_content, font_size=28, color=color)
        
        def create_small_cite(text_content):
            return Text(text_content, font_size=16, color=PRIMARY_ACCENT_COLOR)

        # --- Scene 1: Title & Hook (0–5s) ---
        scene1_elements = VGroup()
        title1 = create_main_title("Could quantum waves break every secret?")
        title2 = create_subtitle("Shor’s Algorithm Revealed")
        cite_text = create_small_cite("Turing, 1940  |  Shor, 1994")

        title1.to_edge(UP, buff=1.5)
        title2.next_to(title1, DOWN, buff=0.4)
        cite_text.to_edge(DOWN, buff=0.5)
        scene1_elements.add(title1, title2, cite_text)

        self.play(FadeIn(title1, shift=DOWN*0.2, run_time=1.0, rate_func=rate_functions.ease_out_sine))
        title2.scale(0.8) # Start smaller for the bounce effect
        self.play(
            Write(title2),
            title2.animate.scale(1.25).set_rate_func(rate_functions.ease_out_bounce), # 1.0 / 0.8 = 1.25
            run_time=0.8
        )
        self.wait(0.5) # Ensure titles are visible before citation
        self.play(FadeIn(cite_text, run_time=0.5))
        self.wait(2.2) # Adjust to fill 5s total: 5 - (1.0 + 0.8 + 0.5 + 0.5) = 2.2
        
        self.play(FadeOut(scene1_elements))

        # --- Scene 2: Historical Timeline (5–20s) ---
        scene2_elements = VGroup()
        timeline = Line(LEFT * 6, RIGHT * 6, color=PRIMARY_ACCENT_COLOR, stroke_width=3)
        scene2_elements.add(timeline)

        events_data = [
            (-5, "1940 · Turing"), 
            (0,  "1977 · RSA"), 
            (5,  "1994 · Shor")
        ]
        
        markers_and_labels = VGroup()
        for x_pos, text_str in events_data:
            dot = Dot(point=[x_pos, 0, 0], color=PRIMARY_ACCENT_COLOR, radius=0.1)
            label = Text(text_str, font_size=22, color=TEXT_COLOR).next_to(dot, DOWN, buff=0.3)
            markers_and_labels.add(VGroup(dot, label))
        
        scene2_elements.add(markers_and_labels)

        self.play(Create(timeline, run_time=0.8))
        self.play(LaggedStart(*[FadeIn(item, shift=UP*0.2) for item in markers_and_labels], lag_ratio=0.5, run_time=1.5))
        self.wait(12.7) # 15s scene: 15 - (0.8 + 1.5) = 12.7
        self.play(FadeOut(scene2_elements))

        # --- Scene 3: Classical Impossibility (20–35s) ---
        scene3_elements = VGroup()
        n15_text = MathTex("N = 15", font_size=60, color=TEXT_COLOR)
        infinity_sym = Text("∞", font_size=90, color=ERROR_COLOR) # Larger infinity
        caption_classical = create_caption("Classical ≈ infinite time")

        n15_text.to_edge(UP, buff=1.5)
        infinity_sym.next_to(n15_text, DOWN, buff=0.8)
        caption_classical.to_edge(DOWN, buff=1.0)
        scene3_elements.add(n15_text, infinity_sym, caption_classical)

        self.play(Write(n15_text, run_time=1.0))
        self.play(FadeIn(infinity_sym, scale=1.5, run_time=0.8)) # Scale in for emphasis
        self.play(infinity_sym.animate.set_rate_func(rate_functions.wiggle).scale(1.1), run_time=1.0) # Pulse
        
        nope_positions = [LEFT * 3 + DOWN * 1, RIGHT * 3 + DOWN * 1]
        for i, pos in enumerate(nope_positions):
            try_text_str = "Try 2x7.. ✕" if i == 0 else "Try 3x5.. ✓" # Show a "correct" one briefly
            try_text_color = ERROR_COLOR if i == 0 else GRAPH_COLOR
            try_text = Text(try_text_str, font_size=28, color=try_text_color).move_to(pos)
            self.play(FadeIn(try_text, run_time=0.3))
            self.wait(0.7 if i == 0 else 1.0) # Hold longer for the "correct" one
            self.play(FadeOut(try_text, run_time=0.3))

        self.play(FadeIn(caption_classical, run_time=0.8))
        self.wait(8.3) # 15s scene: 15 - (1+0.8+1+ (0.3+0.7+0.3)*1 + (0.3+1.0+0.3)*1 +0.8) approx
        self.play(FadeOut(scene3_elements))

        # --- Scene 4: Superposition Spark (35–50s) ---
        scene4_elements = VGroup()
        num_bars = 8
        bars = VGroup(*[
            Rectangle(width=0.7, height=2.5, fill_color=TEXT_COLOR, fill_opacity=1, stroke_width=0)
            for _ in range(num_bars)
        ]).arrange(RIGHT, buff=0.25).shift(UP * 0.5)
        
        bar_labels = VGroup()
        for i in range(num_bars):
            label = MathTex(f"|{i}\\rangle", font_size=24, color=TEXT_COLOR)
            label.next_to(bars[i], DOWN, buff=0.2)
            bar_labels.add(label)
            
        caption_superposition = create_caption("Superposition: All states at once", color=PRIMARY_ACCENT_COLOR)
        caption_superposition.to_edge(DOWN, buff=1.0)
        scene4_elements.add(bars, bar_labels, caption_superposition)

        self.play(LaggedStart(*[GrowFromCenter(bar) for bar in bars], lag_ratio=0.1, run_time=1.0))
        self.play(LaggedStart(*[bar.animate.set_fill(SECONDARY_ACCENT_COLOR, opacity=0.85) for bar in bars], lag_ratio=0.05, run_time=0.8))
        self.play(FadeIn(bar_labels, shift=UP*0.1, lag_ratio=0.1, run_time=0.8))
        self.play(Write(caption_superposition, run_time=1.0))
        self.wait(10.4) # 15s scene: 15 - (1+0.8+0.8+1) = 11.4, adjust based on feel
        self.play(FadeOut(scene4_elements))

        # --- Scene 5: Period Finding (50–65s) ---
        scene5_elements = VGroup()
        ax = Axes(
            x_range=[0, 7.5, 1],  # x from 0 to 7 for 8 points
            y_range=[-1, 15, 5], # y from 0 to 14 for 2^x mod 15
            x_length=10,
            y_length=5,
            axis_config={"include_numbers": True, "font_size": 20, "color": TEXT_COLOR},
            tips=False,
        ).shift(UP*0.2)
        
        points_data = [(x, (2**x) % 15) for x in range(8)] # x from 0 to 7

        # Create the graph line
        graph_line = ax.plot(lambda x: (2**x) % 15, x_range=[0, 7, 0.1], color=GRAPH_COLOR, use_smoothing=False)
        
        # Create dots for vertices
        graph_vertices = VGroup(*[Dot(ax.c2p(x,y), color=PRIMARY_ACCENT_COLOR, radius=0.08) for x,y in points_data])

        moving_dot = Dot(ax.c2p(points_data[0][0], points_data[0][1]), color=ERROR_COLOR, radius=0.12)
        
        period_lines_group = VGroup()
        for x_val in [0, 4]: # Period r=4
            line = DashedLine(ax.c2p(x_val, -1), ax.c2p(x_val, 15), color=PRIMARY_ACCENT_COLOR, stroke_width=2)
            period_lines_group.add(line)

        r_text = MathTex("r=4", font_size=36, color=TEXT_COLOR).next_to(ax, UP, buff=0.3)
        scene5_elements.add(ax, graph_line, graph_vertices, moving_dot, period_lines_group, r_text)

        self.play(Create(ax, run_time=1.0))
        self.play(Create(graph_line, run_time=1.2), FadeIn(graph_vertices, lag_ratio=0.1))
        self.add(moving_dot) # Add dot before animating it

        for x_coord, y_coord in points_data:
            self.play(moving_dot.animate.move_to(ax.c2p(x_coord, y_coord)), run_time=0.4)
        
        self.play(Create(period_lines_group, run_time=0.8))
        self.play(Write(r_text, run_time=0.6))
        self.wait(7.2) # 15s scene: 15-(1+1.2+ (0.4*8) +0.8+0.6) = 7.2
        self.play(FadeOut(scene5_elements))

        # --- Scene 6: QFT “Aha” (65–80s) ---
        scene6_elements = VGroup()
        num_qft_arrows = 8
        qft_arrows = VGroup()
        for i in range(num_qft_arrows):
            arrow = Arrow(ORIGIN, UP, buff=0, stroke_color="#7FFF00", stroke_width=7, max_tip_length_to_length_ratio=0.25)
            arrow.scale(0.8) # Make arrows a bit smaller
            qft_arrows.add(arrow)
        qft_arrows.arrange(RIGHT, buff=0.3).shift(UP * 1.5)
        
        self.play(LaggedStart(*[FadeIn(arr) for arr in qft_arrows], lag_ratio=0.1, run_time=0.8))
        
        # Rotate arrows based on f(x) = 2^x mod 15
        rotation_animations = []
        for i, arr in enumerate(qft_arrows):
            # Phase proportional to f(x_i)
            angle = -2 * PI * ((2**i) % 15) / 15.0 # Negative for clockwise rotation from UP
            rotation_animations.append(Rotate(arr, angle, about_point=arr.get_start(), run_time=0.8))
        self.play(LaggedStart(*rotation_animations, lag_ratio=0.1))
        
        self.wait(0.5) # Pause to see rotated arrows
        
        # "Collapse" arrows to center (simulate QFT input processing)
        self.play(LaggedStart(*[arr.animate.move_to(ORIGIN + DOWN*0.5).scale(0.7) for arr in qft_arrows], lag_ratio=0.05, run_time=0.7))
        self.play(FadeOut(qft_arrows, run_time=0.3))

        # Probability bars for QFT output
        qft_output_bars = VGroup(*[
            Rectangle(width=0.6, height=0.1, fill_color=TEXT_COLOR, fill_opacity=0.7, stroke_width=0) # Start small
            for _ in range(num_qft_arrows)
        ]).arrange(RIGHT, buff=0.25).move_to(DOWN * 1.0)
        
        self.play(Create(qft_output_bars, run_time=0.5))
        
        # Grow peaks at indices 0, 2, 4, 6 (for r=4, N_qft_states=8, peaks at k*N/r = k*8/4 = 2k)
        peak_indices = [0, 2, 4, 6] 
        peak_anims = []
        for idx in peak_indices:
            if idx < len(qft_output_bars): # Safety check
                peak_anims.append(qft_output_bars[idx].animate.stretch_to_fit_height(3.0).set_fill(GRAPH_COLOR))
        
        self.play(LaggedStart(*peak_anims, lag_ratio=0.2, run_time=1.2))
        
        # "Aha" glow on a significant peak (e.g., index 4 or the first non-zero k)
        if 4 < len(qft_output_bars):
            glow_target = qft_output_bars[4]
            glow = SurroundingRectangle(glow_target, color=PRIMARY_ACCENT_COLOR, buff=0.05, stroke_width=4)
            self.play(FadeIn(glow, run_time=0.4))
            self.play(FadeOut(glow, run_time=0.8, rate_func=rate_functions.ease_out_sine))
        
        qft_caption = create_caption("QFT reveals period 'r' in peaks", color=TEXT_COLOR)
        qft_caption.next_to(qft_output_bars, UP, buff=0.4)
        self.play(Write(qft_caption, run_time=0.8))
        scene6_elements.add(qft_output_bars, qft_caption) # Add for cleanup
        
        self.wait(6.8) # 15s scene: 15 - (0.8+0.8+0.5+0.7+0.3+0.5+1.2+0.4+0.8+0.8) = approx 7s
        self.play(FadeOut(scene6_elements))

        # --- Scene 7: Measure & CTA (80–90s) ---
        scene7_elements = VGroup()
        measure_text = Text("Measure k (e.g., k=2)", font_size=40, color=SECONDARY_ACCENT_COLOR).to_edge(UP, buff=1.0)
        
        # Simplified math for r from k (actual math is more nuanced with continued fractions)
        r_calc_text = MathTex("r = N_{QFT} / \\text{gcd}(k, N_{QFT}) \\approx 8/\\text{gcd}(2,8) = 4", font_size=28, color=TEXT_COLOR)
        r_calc_text.next_to(measure_text, DOWN, buff=0.4)
        
        factors_text = MathTex("\\gcd(a^{r/2}\\pm1, N) \\rightarrow \\gcd(2^{4/2}\\pm1, 15) \\rightarrow 3, 5", font_size=28, color=TEXT_COLOR)
        factors_text.next_to(r_calc_text, DOWN, buff=0.3)
        scene7_elements.add(measure_text, r_calc_text, factors_text)

        self.play(Write(measure_text, run_time=0.8))
        self.play(Write(r_calc_text, run_time=1.0))
        self.play(Write(factors_text, run_time=1.0))

        # Flash factors "3" and "5"
        factor_3_highlight = factors_text.get_part_by_tex("3").copy().set_color(GRAPH_COLOR)
        factor_5_highlight = factors_text.get_part_by_tex("5").copy().set_color(GRAPH_COLOR)
        
        self.play(AnimationGroup(
            Indicate(factor_3_highlight, scale_factor=1.5, run_time=0.5),
            Indicate(factor_5_highlight, scale_factor=1.5, run_time=0.5),
            lag_ratio=0.3
        ))
        
        self.wait(0.5) # Hold factors

        cta1_text = create_caption("Hidden rhythms shape our world.")
        cta2_text = Text("What secret will YOU unlock?", font_size=40, color=PRIMARY_ACCENT_COLOR, weight=BOLD)
        cta1_text.next_to(factors_text, DOWN, buff=0.8)
        cta2_text.next_to(cta1_text, DOWN, buff=0.4)
        scene7_elements.add(cta1_text, cta2_text)

        self.play(Write(cta1_text, run_time=0.8))
        cta2_text.scale(0.8) # For bounce effect
        self.play(
            Write(cta2_text),
            cta2_text.animate.scale(1.25).set_rate_func(rate_functions.ease_out_bounce),
            run_time=0.8
        )

        # Sparkles
        sparkles_group = VGroup()
        sparkle_animations = []
        for _ in range(25):
            sparkle = Dot(radius=random.uniform(0.02, 0.06), color=random_bright_color())
            # Corrected lines using config:
            sparkle.move_to([random.uniform(-config.frame_width/2 + 1, config.frame_width/2 - 1), 
                             random.uniform(-config.frame_height/2 + 1, config.frame_height/2 - 1), 0])
            sparkles_group.add(sparkle)
            sparkle_animations.append(Succession(
                FadeIn(sparkle, scale=0.5, run_time=random.uniform(0.2, 0.5)),
                FadeOut(sparkle, scale=0.5, run_time=random.uniform(0.2, 0.5))
            ))
        self.play(LaggedStart(*sparkle_animations, lag_ratio=0.03))
        
        logo_text = Text("⚛ Harvard Quantum Shorts", font_size=28, color="#A51C30") # Harvard Crimson
        logo_text.to_edge(DOWN, buff=0.4)
        scene7_elements.add(logo_text)
        self.play(FadeIn(logo_text, run_time=0.8))

        self.wait(1.1) # 10s scene: 10 - (0.8+1+1+0.5+0.5+0.8+0.8+(0.03*25*0.4)+0.8) approx
        
        self.play(FadeOut(scene7_elements, run_time=1.0))
        self.wait(1.0) # Final pause