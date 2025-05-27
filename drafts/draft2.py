from manim import *
import random

# --- Style Configuration ---
DARK_BACKGROUND_COLOR = "#090d1a" # Consistent deep blue-grey
TEXT_COLOR = WHITE
PRIMARY_ACCENT_COLOR = "#FFD700"  # Gold
SECONDARY_ACCENT_COLOR = "#38a3a5" # Teal
GRAPH_COLOR = "#00FF00"   # Bright Green
ERROR_COLOR = "#FF3333"   # Red
CRIMSON_COLOR = "#A51C30" # For Harvard logo

# --- Pixel to Manim Coordinate Helpers ---
PIXEL_WIDTH = 1920
PIXEL_HEIGHT = 1080

def px_to_manim_y(px_y_from_top):
    return (PIXEL_HEIGHT / 2 - px_y_from_top) * config.frame_height / PIXEL_HEIGHT

def px_to_manim_x(px_x_from_left):
    return (px_x_from_left - PIXEL_WIDTH / 2) * config.frame_width / PIXEL_WIDTH

class QuantumEncryptionVideoEnhanced(Scene):
    def construct(self):
        self.camera.background_color = DARK_BACKGROUND_COLOR # Set once for all scenes

        def create_text_panel(text_mobject, padding=0.1, opacity=0.65, color=BLACK):
            panel = Rectangle(
                width=text_mobject.width + 2 * padding,
                height=text_mobject.height + 2 * padding,
                fill_color=color,
                fill_opacity=opacity,
                stroke_width=0
            ).move_to(text_mobject.get_center()).set_z_index(text_mobject.z_index - 1)
            return VGroup(panel, text_mobject)

        # --- ⏱️ 0 – 5 s TITLE & OPENING HOOK ---
        scene1_elements = VGroup()
        title1_text_str = "Could quantum waves break every secret?"
        title1 = Text(title1_text_str, font_size=60, color=TEXT_COLOR, weight=BOLD)
        title1.move_to(np.array([0, px_to_manim_y(700), 0]))
        title2_text_str = "Shor’s Algorithm Revealed"
        title2 = Text(title2_text_str, font_size=32, color=PRIMARY_ACCENT_COLOR)
        title2.move_to(np.array([0, px_to_manim_y(640), 0]))
        citation_text_str = "Turing 1940 • RSA 1977 • Shor 1994"
        citation = Text(citation_text_str, font_size=16, color=PRIMARY_ACCENT_COLOR)
        citation.move_to(np.array([0, px_to_manim_y(PIXEL_HEIGHT - 50), 0]))
        scene1_elements.add(title1, title2, citation)

        self.play(FadeIn(title1, run_time=1.0, rate_func=rate_functions.ease_in_sine))
        title2.scale(0.8)
        self.play(
            Write(title2),
            title2.animate.scale(1.25).set_rate_func(rate_functions.ease_out_bounce),
            run_time=0.8
        )
        self.wait(3.5 - (1.0 + 0.8))
        self.play(FadeIn(citation, run_time=0.5))
        self.wait(5.0 - (3.5 + 0.5))
        self.play(FadeOut(scene1_elements, run_time=0.5, rate_func=rate_functions.ease_out_sine))
        self.wait(0.1)

        # --- ⏱️ 5 – 20 s SCENE 1: HISTORICAL TIMELINE ---
        scene2_elements = VGroup()
        timeline_y_manim = px_to_manim_y(400)
        timeline_start_x_manim = px_to_manim_x(200)
        timeline_end_x_manim = px_to_manim_x(PIXEL_WIDTH - 200)
        timeline = Line(
            start=np.array([timeline_start_x_manim, timeline_y_manim, 0]),
            end=np.array([timeline_end_x_manim, timeline_y_manim, 0]),
            color=PRIMARY_ACCENT_COLOR, stroke_width=3
        )
        scene2_elements.add(timeline)
        events_data = [
            (px_to_manim_x(240), "1940·Turing", 0.0),
            (px_to_manim_x(960), "1977·RSA", 0.2),
            (px_to_manim_x(1680), "1994·Shor", 0.4)
        ]
        markers_and_labels = VGroup()
        for x_manim, text_str, delay in events_data:
            dot = Dot(point=[x_manim, timeline_y_manim, 0], color=PRIMARY_ACCENT_COLOR, radius=0.1)
            label = Text(text_str, font_size=24, color=TEXT_COLOR).next_to(dot, DOWN, buff=0.3)
            event_group = VGroup(dot, label)
            markers_and_labels.add(event_group)
        scene2_elements.add(markers_and_labels)

        self.play(Create(timeline, run_time=0.8, rate_func=rate_functions.ease_in_out_sine))
        animation_sequence = []
        current_delay_tracker = 0.8 
        for i, event_group in enumerate(markers_and_labels):
            event_delay = events_data[i][2]
            animation_sequence.append(Wait(event_delay))
            animation_sequence.append(FadeIn(event_group, shift=UP*0.2, run_time=0.5, rate_func=rate_functions.ease_out_sine))
            current_delay_tracker += event_delay + 0.5
        self.play(Succession(*animation_sequence))
        self.wait(15.0 - (0.5 + current_delay_tracker)) 
        self.play(FadeOut(scene2_elements, run_time=0.5, rate_func=rate_functions.ease_out_sine))
        self.wait(0.1)

        # --- ⏱️ 20 – 35 s SCENE 2: CLASSICAL IMPOSSIBILITY ---
        scene3_elements = VGroup()
        original_bg_color_scene3 = self.camera.background_color 
        self.camera.background_color = "#222222" 

        n15_latex = MathTex("N = 15", font_size=64, color=TEXT_COLOR)
        n15_latex.move_to(np.array([0, px_to_manim_y(600), 0]))
        infinity_sym = Text("∞", font_size=90, color=ERROR_COLOR)
        infinity_sym.move_to(np.array([0, px_to_manim_y(420), 0]))
        caption_classical = Text("Classical ≈ infinite time", font_size=28, color=TEXT_COLOR)
        caption_classical.move_to(np.array([0, px_to_manim_y(PIXEL_HEIGHT - 240), 0]))
        scene3_elements.add(n15_latex, infinity_sym, caption_classical)

        self.play(Write(n15_latex, run_time=1.0, rate_func=rate_functions.ease_out_sine))
        self.play(FadeIn(infinity_sym, run_time=0.5, rate_func=rate_functions.ease_in_sine),
                  infinity_sym.animate(run_time=0.5, rate_func=rate_functions.wiggle).scale(1.1))
        
        time_elapsed_in_scene3 = 1.0 + 0.5 
        
        wait_for_flash1 = (5.0) - time_elapsed_in_scene3 
        self.wait(wait_for_flash1)
        time_elapsed_in_scene3 += wait_for_flash1
        flash1_text = Text("Try 3×5… ✕", font_size=32, color=ERROR_COLOR)
        flash1_panel = create_text_panel(flash1_text.move_to(LEFT*3.5), padding=0.15)
        self.play(FadeIn(flash1_panel, run_time=0.3, rate_func=rate_functions.linear))
        self.play(FadeOut(flash1_panel, run_time=0.3, rate_func=rate_functions.linear))
        time_elapsed_in_scene3 += 0.3+0.3

        wait_for_flash2 = (9.0) - time_elapsed_in_scene3 
        self.wait(wait_for_flash2)
        time_elapsed_in_scene3 += wait_for_flash2
        flash2_text = Text("Try 5×3… ✓", font_size=32, color=GRAPH_COLOR)
        flash2_panel = create_text_panel(flash2_text.move_to(RIGHT*3.5), padding=0.15)
        self.play(FadeIn(flash2_panel, run_time=0.3, rate_func=rate_functions.linear))
        self.play(FadeOut(flash2_panel, run_time=0.3, rate_func=rate_functions.linear))
        time_elapsed_in_scene3 += 0.3+0.3

        self.play(FadeIn(caption_classical, run_time=0.8, rate_func=rate_functions.ease_out_sine))
        time_elapsed_in_scene3 += 0.8
        
        self.wait(15.0 - time_elapsed_in_scene3 - 0.5) 
        self.play(FadeOut(scene3_elements, run_time=0.5, rate_func=rate_functions.ease_out_sine))
        self.camera.background_color = original_bg_color_scene3 
        self.wait(0.1)

        # --- ⏱️ 35 – 50 s SCENE 3: SUPERPOSITION SPARK ---
        scene4_elements = VGroup()
        num_bars = 8
        bars_y_manim = px_to_manim_y(500) 
        bar_height = 2.5
        bars = VGroup(*[
            Rectangle(width=0.7, height=bar_height, fill_color=TEXT_COLOR, fill_opacity=1, stroke_width=0)
            for _ in range(num_bars)
        ]).arrange(RIGHT, buff=0.25).move_to(np.array([0, bars_y_manim, 0])) 
        
        for bar in bars:
            bar.move_to(bar.get_bottom() + UP * bar_height / 2, aligned_edge=DOWN)

        bar_labels = VGroup()
        for i in range(num_bars):
            label = MathTex(f"|{i}\\rangle", font_size=24, color=TEXT_COLOR)
            label.next_to(bars[i], DOWN, buff=0.2) 
            bar_labels.add(label)
            
        caption_superposition_str = "Superposition = all states at once"
        caption_superposition = Text(caption_superposition_str, font_size=32, color=PRIMARY_ACCENT_COLOR)
        caption_superposition.move_to(np.array([0, px_to_manim_y(300), 0]))
        caption_panel = create_text_panel(caption_superposition, padding=0.15)
        scene4_elements.add(bars, bar_labels, caption_panel)

        self.play(LaggedStart(*[GrowFromCenter(bar, run_time=1.0, rate_func=rate_functions.ease_out_expo) for bar in bars], lag_ratio=0.1))
        self.play(LaggedStart(*[bar.animate.set_fill(SECONDARY_ACCENT_COLOR, opacity=0.85) for bar in bars], lag_ratio=0.05, run_time=0.4, rate_func=rate_functions.linear))
        self.play(FadeIn(bar_labels, shift=UP*0.1, lag_ratio=0.1, run_time=0.6, rate_func=rate_functions.ease_out_sine))
        self.play(Write(caption_panel, run_time=1.0, rate_func=rate_functions.ease_out_sine))
        self.wait(15.0 - (1.0 + 0.4 + 0.6 + 1.0 + 0.5)) 
        self.play(FadeOut(scene4_elements, run_time=0.5, rate_func=rate_functions.ease_out_sine))
        self.wait(0.1)

        # --- ⏱️ 50 – 65 s SCENE 4: PERIOD FINDING ---
        scene5_elements = VGroup()
        axes_y_manim = px_to_manim_y(450)
        ax = Axes(
            x_range=[0, 7.5, 1], y_range=[-1, 15, 5],
            x_length=10, y_length=5,
            axis_config={"include_numbers": True, "font_size": 20, "color": TEXT_COLOR},
            tips=False, 
        ).move_to(np.array([0, axes_y_manim, 0]))
        points_data = [(x, (2**x) % 15) for x in range(8)]
        graph_line = ax.plot(lambda x: (2**x) % 15, x_range=[0, 7, 0.1], color=GRAPH_COLOR, use_smoothing=False)
        graph_vertices = VGroup(*[Dot(ax.c2p(x,y), color=PRIMARY_ACCENT_COLOR, radius=0.08) for x,y in points_data])
        moving_dot = Dot(ax.c2p(points_data[0][0], points_data[0][1]), color=ERROR_COLOR, radius=0.12)
        bracket_y_bottom = ax.c2p(0, -0.5)[1]
        bracket_y_top = ax.c2p(0, 14.5)[1]
        bracket1 = BraceBetweenPoints(np.array([ax.c2p(0,0)[0], bracket_y_bottom,0]), np.array([ax.c2p(0,0)[0], bracket_y_top,0]), direction=LEFT, color=PRIMARY_ACCENT_COLOR)
        bracket2 = BraceBetweenPoints(np.array([ax.c2p(4,0)[0], bracket_y_bottom,0]), np.array([ax.c2p(4,0)[0], bracket_y_top,0]), direction=LEFT, color=PRIMARY_ACCENT_COLOR)
        r_text = MathTex("r=4", font_size=36, color=TEXT_COLOR).next_to(ax, UP, buff=0.3)
        r_text_panel = create_text_panel(r_text, padding=0.1)
        scene5_elements.add(ax, graph_line, graph_vertices, moving_dot, bracket1, bracket2, r_text_panel)

        if self.mobjects: 
            self.play(FadeOut(*self.mobjects.copy(), run_time=0.5, rate_func=rate_functions.ease_out_sine))
        
        self.play(Create(ax, run_time=1.0, rate_func=rate_functions.ease_in_out_sine))
        self.play(Create(graph_line, run_time=1.2, rate_func=rate_functions.ease_in_out_sine), 
                  FadeIn(graph_vertices, lag_ratio=0.1, run_time=0.8, rate_func=rate_functions.ease_out_sine))
        self.add(moving_dot)
        dot_hop_animations = []
        for x_coord, y_coord in points_data:
            dot_hop_animations.append(moving_dot.animate(run_time=0.4, rate_func=rate_functions.ease_in_out_sine).move_to(ax.c2p(x_coord, y_coord)))
        self.play(Succession(*dot_hop_animations))
        self.play(Create(bracket1, run_time=0.4, rate_func=rate_functions.ease_out_sine))
        self.play(Create(bracket2, run_time=0.4, rate_func=rate_functions.ease_out_sine))
        self.play(Write(r_text_panel, run_time=0.6, rate_func=rate_functions.ease_out_sine))
        self.wait(15.0 - (0.5+1.0+1.2+0.8 + (0.4*len(points_data)) + 0.4+0.4+0.6 + 0.5)) 
        self.play(FadeOut(scene5_elements, run_time=0.5, rate_func=rate_functions.ease_out_sine))
        self.wait(0.1)

        # --- ⏱️ 65 – 80 s SCENE 5: QFT WAVE INTERFERENCE “AHA” ---
        scene6_elements = VGroup()
        wave_axes_height = 2.0
        wave_x_range = [0, 8]
        axes_components = Axes(
            x_range=wave_x_range + [1], y_range=[-1.5, 1.5, 1],
            x_length=10, y_length=wave_axes_height * 1.2, 
            axis_config={"include_numbers": True, "font_size":20, "color": TEXT_COLOR}, 
            tips=False,
        ).to_edge(UP, buff=0.3)
        scene6_elements.add(axes_components)
        axes_sum = Axes(
            x_range=wave_x_range + [1], y_range=[-3.5, 3.5, 1],
            x_length=10, y_length=wave_axes_height, 
            axis_config={"include_numbers": True, "font_size":20, "color": TEXT_COLOR},
            tips=False,
        ).next_to(axes_components, DOWN, buff=0.5)
        scene6_elements.add(axes_sum)
        time_tracker = ValueTracker(0) 
        speed = 0.6 * PI 
        k_period_4 = TAU / 4.0
        fx_amplitudes = [((2**i)%15)/15.0 * 0.8 + 0.2 for i in range(3)] 
        fx_phases = [PI/3 * ((2**i)%3) for i in range(3)] 

        def wave1_func(x): return fx_amplitudes[0] * np.sin(k_period_4 * x - speed * time_tracker.get_value() + fx_phases[0])
        def wave2_func(x): return fx_amplitudes[1] * np.sin(k_period_4 * x - speed * time_tracker.get_value() + fx_phases[1])
        def wave3_func(x): return fx_amplitudes[2] * np.sin(k_period_4 * x - speed * time_tracker.get_value() + fx_phases[2])
        def sum_wave_func(x): return wave1_func(x) + wave2_func(x) + wave3_func(x)
        
        plot_w1 = axes_components.plot(wave1_func, color=BLUE_D, use_smoothing=True)
        plot_w2 = axes_components.plot(wave2_func, color=TEAL_D, use_smoothing=True)
        plot_w3 = axes_components.plot(wave3_func, color=GREEN_D, use_smoothing=True)
        plot_sum = axes_sum.plot(sum_wave_func, color=GRAPH_COLOR, stroke_width=4, use_smoothing=True)
        
        plots_and_their_axes = [
            (plot_w1, wave1_func, axes_components),
            (plot_w2, wave2_func, axes_components),
            (plot_w3, wave3_func, axes_components),
            (plot_sum, sum_wave_func, axes_sum)
        ]

        for plot_obj, func_def, associated_axes_object in plots_and_their_axes:
            plot_obj.add_updater(
                lambda mob, dt, f=func_def, ax_obj=associated_axes_object: mob.become(
                    ax_obj.plot(f, color=mob.get_color(), stroke_width=mob.get_stroke_width(), use_smoothing=True)
                )
            )
        scene6_elements.add(plot_w1, plot_w2, plot_w3, plot_sum)

        if self.mobjects:
            self.play(FadeOut(*self.mobjects.copy(), run_time=0.5, rate_func=rate_functions.ease_out_sine))
            
        self.play(Create(axes_components, run_time=1.0, rate_func=rate_functions.ease_in_out_sine), 
                  Create(axes_sum, run_time=1.0, rate_func=rate_functions.ease_in_out_sine),
                  Create(plot_w1, run_time=1.0, rate_func=rate_functions.ease_in_out_sine), 
                  Create(plot_w2, run_time=1.0, rate_func=rate_functions.ease_in_out_sine), 
                  Create(plot_w3, run_time=1.0, rate_func=rate_functions.ease_in_out_sine),
                  Create(plot_sum, run_time=1.0, rate_func=rate_functions.ease_in_out_sine))
        
        self.play(time_tracker.animate(rate_func=linear).set_value(4), run_time=4.0) 
        
        x_peak_val = 4.0 
        if axes_sum.x_range[0] <= x_peak_val <= axes_sum.x_range[1]:
            y_peak_val_sum = sum_wave_func(x_peak_val) 
            peak_point_sum = axes_sum.c2p(x_peak_val, y_peak_val_sum)
            pulse_dot = Dot(peak_point_sum, color=PRIMARY_ACCENT_COLOR, radius=0.01) 
            pulse_ring = Circle(radius=0.01, color=PRIMARY_ACCENT_COLOR, stroke_width=3).move_to(peak_point_sum)
            self.add(pulse_dot, pulse_ring) 
            self.play(Transform(pulse_dot, Dot(peak_point_sum, color=PRIMARY_ACCENT_COLOR, radius=0.15), run_time=0.4, rate_func=rate_functions.ease_out_sine),
                      Transform(pulse_ring, Circle(radius=0.3, color=PRIMARY_ACCENT_COLOR, stroke_width=4).move_to(peak_point_sum), run_time=0.4, rate_func=rate_functions.ease_out_sine))
            self.play(FadeOut(pulse_dot, run_time=0.4, rate_func=rate_functions.ease_in_sine), 
                      FadeOut(pulse_ring, run_time=0.4, rate_func=rate_functions.ease_in_sine))
            
        caption_qft_str = "QFT = Wave interference → period"
        caption_qft = Text(caption_qft_str, font_size=32, color=TEXT_COLOR)
        caption_qft_panel = create_text_panel(caption_qft.to_edge(UP, buff=0.1), padding=0.15)
        scene6_elements.add(caption_qft_panel)
        self.play(Write(caption_qft_panel, run_time=0.8, rate_func=rate_functions.ease_out_sine))
        self.wait(15.0 - (0.5 + 1.0 + 4.0 + 0.4 + 0.4 + 0.8 + 0.5)) 
        for p_obj, _, _ in plots_and_their_axes: p_obj.clear_updaters() 
        self.play(FadeOut(scene6_elements, run_time=0.5, rate_func=rate_functions.ease_out_sine))
        self.wait(0.1)

        # --- ⏱️ 80 – 90 s SCENE 6: MEASURE & CALL TO ACTION ---
        scene7_elements = VGroup()
        
        if self.mobjects:
            self.play(FadeOut(*self.mobjects.copy(), run_time=0.5, rate_func=rate_functions.ease_out_sine))

        k_text_str = "k = 2"
        k_text = Text(k_text_str, font_size=48, color=SECONDARY_ACCENT_COLOR)
        k_text_panel = create_text_panel(k_text.to_edge(UP, buff=1.0), padding=0.15)
        scene7_elements.add(k_text_panel)
        formula1_str = "r = 8 \\times 2^{-1} \\pmod 8 = 4"
        formula1 = MathTex(formula1_str, font_size=28, color=TEXT_COLOR)
        formula1_panel = create_text_panel(formula1.next_to(k_text_panel, DOWN, buff=0.4), padding=0.1)
        scene7_elements.add(formula1_panel)
        formula2_str = "\\gcd(2^{4/2}\\pm1, 15) \\rightarrow 3, 5"
        formula2 = MathTex(formula2_str, font_size=28, color=TEXT_COLOR) 
        formula2_panel = create_text_panel(formula2.next_to(formula1_panel, DOWN, buff=0.3), padding=0.1)
        scene7_elements.add(formula2_panel)

        self.play(FadeIn(k_text_panel, run_time=0.6, rate_func=rate_functions.ease_out_sine))
        self.play(Write(formula1_panel, run_time=1.0, rate_func=rate_functions.ease_out_sine))
        self.play(Write(formula2_panel, run_time=1.0, rate_func=rate_functions.ease_out_sine))
        
        factor_3_highlight = formula2.get_part_by_tex("3").copy().set_color(GRAPH_COLOR)
        factor_5_highlight = formula2.get_part_by_tex("5").copy().set_color(GRAPH_COLOR)
        self.play(
            Succession(
                Indicate(factor_3_highlight, scale_factor=1.7, run_time=0.5, rate_func=rate_functions.there_and_back_with_pause),
                Wait(0.1),
                Indicate(factor_5_highlight, scale_factor=1.7, run_time=0.5, rate_func=rate_functions.there_and_back_with_pause)
            )
        )
        
        cta1_str = "Hidden rhythms shape our world."
        cta1 = Text(cta1_str, font_size=36, color=TEXT_COLOR)
        cta1.move_to(np.array([0, px_to_manim_y(PIXEL_HEIGHT - 400), 0])) 
        cta1_panel = create_text_panel(cta1, padding=0.15)
        scene7_elements.add(cta1_panel)
        cta2_str = "What secret will YOU unlock?"
        cta2 = Text(cta2_str, font_size=48, color=PRIMARY_ACCENT_COLOR, weight=BOLD)
        cta2.next_to(cta1_panel, DOWN, buff=0.5) 
        scene7_elements.add(cta2) 

        self.play(FadeIn(cta1_panel, run_time=0.8, rate_func=rate_functions.ease_out_sine))
        cta2.scale(0.8)
        self.play(
            Write(cta2), 
            cta2.animate.scale(1.25).set_rate_func(rate_functions.ease_out_bounce),
            run_time=0.8
        )
        
        sparkles_group = VGroup()
        sparkle_animations = []
        num_sparkles = 15
        sparkle_duration = 2.0
        logo_fadein_duration = 0.8
        
        time_for_text_anims = 0.6 + 1.0 + 1.0 + (0.5*2+0.1) + 0.8 + 0.8 
        total_anim_time_budget = 9.5 
        
        wait_before_sparkles_start = total_anim_time_budget - time_for_text_anims - sparkle_duration
        if wait_before_sparkles_start < 0: wait_before_sparkles_start = 0.05

        self.wait(wait_before_sparkles_start)

        for _ in range(num_sparkles):
            # Corrected sparkle color generation
            sparkle_grey_shade = random.uniform(0.7, 1.0) 
            sparkle = Dot(radius=random.uniform(0.02, 0.05), color=rgb_to_color([sparkle_grey_shade, sparkle_grey_shade, sparkle_grey_shade]))
            sparkle.move_to([random.uniform(-config.frame_width/2.5, config.frame_width/2.5), 
                             random.uniform(cta2.get_bottom()[1] - 1.0, cta1.get_top()[1] + 1.0), 0]) 
            sparkles_group.add(sparkle) 
            sparkle_animations.append(Succession(
                FadeIn(sparkle, scale=0.5, run_time=random.uniform(0.3, 0.6)),
                FadeOut(sparkle, scale=0.5, run_time=random.uniform(0.3, 0.6))
            ))
        
        self.play(
            LaggedStart(*sparkle_animations, lag_ratio=(sparkle_duration / num_sparkles) * 0.7),
            run_time=sparkle_duration
        )
        scene7_elements.add(sparkles_group) 
        
        logo_str = "⚛ Harvard Quantum Shorts"
        logo = Text(logo_str, font_size=32, color=CRIMSON_COLOR)
        logo.move_to(np.array([0, px_to_manim_y(PIXEL_HEIGHT - 100), 0]))
        logo_panel = create_text_panel(logo, padding=0.1)
        scene7_elements.add(logo_panel)
        
        self.play(
            AnimationGroup(
                Wait(sparkle_duration - logo_fadein_duration if sparkle_duration > logo_fadein_duration else 0.01), 
                FadeIn(logo_panel, run_time=logo_fadein_duration, rate_func=rate_functions.ease_out_sine),
                lag_ratio=1 
            )
        )
        
        self.wait(0.1) 

        self.play(FadeOut(scene7_elements, run_time=0.5, rate_func=rate_functions.ease_out_sine))
        self.wait(0.5)