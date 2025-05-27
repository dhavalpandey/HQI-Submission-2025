from manim import *
import random

# --- Style Configuration ---
DARK_BACKGROUND_COLOR = "#090d1a" # Consistent deep blue-grey
TEXT_COLOR = WHITE
PRIMARY_ACCENT_COLOR = "#FFD700"  # Gold
SECONDARY_ACCENT_COLOR = "#38a3a5" # Teal
GRAPH_COLOR = "#00FF00"   # Bright Green
ERROR_COLOR = "#FF3333"   # Red
CRIMSON_COLOR = "#A51C30" # For Harvard logo (though removed from end)
ICON_COLOR = WHITE

# --- Pixel to Manim Coordinate Helpers ---
# (Assuming default Manim frame size which is usually -7.11 to 7.11 H, -4 to 4 V)
# These helpers might need adjustment if your config.frame_width/height are different
# or if pixel coordinates are from a specific design canvas.
# For simplicity, I'll use relative positioning (to_edge, next_to, move_to with Manim units)
# where explicit pixel coordinates are not strictly necessary or can be translated.

class QuantumEncryptionVideoEnhanced(Scene):
    def construct(self):
        self.camera.background_color = DARK_BACKGROUND_COLOR # Set once for all scenes

        def create_text_panel(text_mobject, padding=0.1, opacity=0.60, color=DARK_BACKGROUND_COLOR, stroke_color=PRIMARY_ACCENT_COLOR, stroke_width=0): # Adjusted defaults
            panel_fill_color = color if color != DARK_BACKGROUND_COLOR else ManimColor(DARK_BACKGROUND_COLOR).interpolate(BLACK, 0.3)

            panel = Rectangle(
                width=text_mobject.width + 2 * padding,
                height=text_mobject.height + 2 * padding,
                fill_color=panel_fill_color,
                fill_opacity=opacity,
                stroke_width=stroke_width,
                stroke_color=stroke_color
            ).move_to(text_mobject.get_center()).set_z_index(text_mobject.z_index - 1)
            return VGroup(panel, text_mobject)

        # --- Revised Opening “Hook” (0–7 s) ---
        hook_elements = VGroup()
        
        icon_scale = 0.6
        email_icon = Text("✉", font_size=96, color=ICON_COLOR).scale(icon_scale) 
        dollar_icon = Text("$", font_size=96, color=ICON_COLOR, weight=BOLD).scale(icon_scale)
        shield_icon = Text("🛡", font_size=96, color=ICON_COLOR).scale(icon_scale) 
        
        icons = VGroup(email_icon, dollar_icon, shield_icon).arrange(RIGHT, buff=1.0).move_to(ORIGIN)
        hook_elements.add(icons)

        self.play(FadeIn(email_icon, run_time=0.5, rate_func=rate_functions.ease_out_sine))
        self.wait(0.5) 
        self.play(FadeIn(dollar_icon, run_time=0.5, rate_func=rate_functions.ease_out_sine))
        self.wait(0.5) 
        self.play(FadeIn(shield_icon, run_time=0.5, rate_func=rate_functions.ease_out_sine))
        
        self.wait(0.2) 
        
        number_2048 = Text("2048", font_size=300, color=TEXT_COLOR, weight=BOLD)
        number_2048.set_opacity(0.0) 
        number_2048.move_to(ORIGIN).set_z_index(email_icon.z_index - 1) 
        hook_elements.add(number_2048)

        lock_icon = Text("🔒", font_size=120, color=ERROR_COLOR) 
        lock_icon.move_to(ORIGIN).set_z_index(number_2048.z_index + 1) 
        hook_elements.add(lock_icon)

        self.play(
            number_2048.animate.set_opacity(0.3).scale(1.5, about_point=ORIGIN), 
            run_time=1.5, 
            rate_func=rate_functions.ease_in_out_sine
        ) 
        
        self.play(FadeIn(lock_icon, scale=0.5, run_time=0.3, rate_func=rate_functions.ease_out_back))
        self.play(Indicate(lock_icon, scale_factor=1.2, color=RED_B, repetitions=2, run_time=0.5, rate_func=rate_functions.there_and_back_with_pause)) 
        
        hook_text_str = "Or could quantum waves break every secret?"
        hook_text = Text(hook_text_str, font_size=60, color=TEXT_COLOR, weight=BOLD)
        hook_text.to_edge(UP, buff=1.5) 
        
        glow_effect = hook_text.copy().set_stroke(PRIMARY_ACCENT_COLOR, width=8, opacity=0.7).set_z_index(hook_text.z_index-1)
        
        self.play(
            FadeIn(hook_text, shift=DOWN*0.1, run_time=1.0, rate_func=rate_functions.ease_out_sine),
            FadeIn(glow_effect, shift=DOWN*0.1, run_time=1.0, rate_func=rate_functions.ease_out_sine),
            FadeOut(icons, lock_icon, number_2048, run_time=0.8, rate_func=rate_functions.ease_in_sine) 
        ) 
        hook_elements.add(hook_text, glow_effect) 
        
        self.wait(7.0 - (2.5 + 0.2 + 1.5 + 0.3 + 0.5 + 1.0)) # Adjust wait to fill 7s
        
        self.play(FadeOut(hook_elements, run_time=0.5, rate_func=rate_functions.ease_out_sine)) 
        self.wait(0.1)

        # --- SCENE 1: HISTORICAL TIMELINE (Now starts effectively after the hook) ---
        # Timeline: 7s to 20s (13s duration)
        scene2_elements = VGroup()
        timeline_y_pos = 0.5 
        timeline = Line(LEFT * 6, RIGHT * 6, color=PRIMARY_ACCENT_COLOR, stroke_width=3).move_to(UP * timeline_y_pos)
        scene2_elements.add(timeline)

        events_data = [
            (LEFT * 5, "1940·Turing", 0.0),
            (ORIGIN, "1977·RSA", 0.2),
            (RIGHT * 5, "1994·Shor", 0.4)
        ]
        
        markers_and_labels = VGroup()
        for x_pos_obj, text_str, delay in events_data:
            point_on_timeline = timeline.point_from_proportion( (x_pos_obj[0] - timeline.get_start()[0]) / timeline.get_length() if timeline.get_length() > 0 else 0.5 )
            dot = Dot(point=point_on_timeline, color=PRIMARY_ACCENT_COLOR, radius=0.1)
            label = Text(text_str, font_size=24, color=TEXT_COLOR).next_to(dot, DOWN, buff=0.35)
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
        
        self.wait(13.0 - current_delay_tracker - 0.5) 
        self.play(FadeOut(scene2_elements, run_time=0.5, rate_func=rate_functions.ease_out_sine))
        self.wait(0.1)


        # --- SCENE 2: CLASSICAL IMPOSSIBILITY (20s – 35s) ---
        scene3_elements = VGroup()
        original_bg_color_scene3 = self.camera.background_color 
        self.camera.background_color = "#222222" 

        n15_latex = MathTex("N = 15", font_size=64, color=TEXT_COLOR).to_edge(UP, buff=1.0)
        infinity_sym = Text("∞", font_size=90, color=ERROR_COLOR).next_to(n15_latex, DOWN, buff=0.8)
        caption_classical = Text("Classical ≈ infinite time", font_size=28, color=TEXT_COLOR).to_edge(DOWN, buff=1.2)
        scene3_elements.add(n15_latex, infinity_sym, caption_classical)

        self.play(Write(n15_latex, run_time=1.0, rate_func=rate_functions.ease_out_sine))
        self.play(FadeIn(infinity_sym, run_time=0.5, rate_func=rate_functions.ease_in_sine),
                  infinity_sym.animate(run_time=0.5, rate_func=rate_functions.wiggle).scale(1.1))
        
        time_elapsed_in_scene3 = 1.0 + 0.5 
        
        wait_for_flash1 = 5.0 - time_elapsed_in_scene3 
        self.wait(wait_for_flash1)
        time_elapsed_in_scene3 += wait_for_flash1
        flash1_text = Text("Try 3×5… ✕", font_size=32, color=ERROR_COLOR) 
        flash1_panel = create_text_panel(flash1_text.move_to(LEFT*3.5 + DOWN*0.5), padding=0.15)
        self.play(FadeIn(flash1_panel, run_time=0.3))
        self.wait(1.0) 
        self.play(FadeOut(flash1_panel, run_time=0.3))
        time_elapsed_in_scene3 += 0.3+1.0+0.3

        wait_for_flash2 = 9.0 - time_elapsed_in_scene3 
        self.wait(wait_for_flash2)
        time_elapsed_in_scene3 += wait_for_flash2
        flash2_text = Text("Try 5×3… ✓", font_size=32, color=GRAPH_COLOR) 
        flash2_panel = create_text_panel(flash2_text.move_to(RIGHT*3.5 + DOWN*0.5), padding=0.15)
        self.play(FadeIn(flash2_panel, run_time=0.3))
        self.wait(1.2) 
        self.play(FadeOut(flash2_panel, run_time=0.3))
        time_elapsed_in_scene3 += 0.3+1.2+0.3

        self.play(FadeIn(caption_classical, run_time=0.8, rate_func=rate_functions.ease_out_sine))
        time_elapsed_in_scene3 += 0.8
        
        self.wait(15.0 - time_elapsed_in_scene3 - 0.5) 
        self.play(FadeOut(scene3_elements, run_time=0.5, rate_func=rate_functions.ease_out_sine))
        self.camera.background_color = original_bg_color_scene3 
        self.wait(0.1)

        # --- SCENE 3: SUPERPOSITION SPARK (35s – 50s) ---
        scene4_elements = VGroup()
        num_bars = 8
        bar_area_center_y = 0.5 
        bar_height = 2.5
        bars = VGroup(*[
            Rectangle(width=0.7, height=bar_height, fill_color=TEXT_COLOR, fill_opacity=1, stroke_width=0)
            for _ in range(num_bars)
        ]).arrange(RIGHT, buff=0.25).move_to(UP * bar_area_center_y)
        
        for bar in bars: 
            bar.move_to(bar.get_bottom() + UP * bar_height / 2, aligned_edge=DOWN)

        bar_labels = VGroup()
        for i in range(num_bars):
            label = MathTex(f"|{i}\\rangle", font_size=28, color=TEXT_COLOR) 
            label.next_to(bars[i], DOWN, buff=0.3) 
            bar_labels.add(label)
        
        bar_labels.next_to(bars, DOWN, buff=0.5) 

        caption_superposition_str = "Superposition = all states at once"
        caption_superposition = Text(caption_superposition_str, font_size=32, color=PRIMARY_ACCENT_COLOR)
        caption_superposition.to_edge(DOWN, buff=0.7) 
        caption_panel = create_text_panel(caption_superposition, padding=0.15, opacity=0.7) 
        
        scene4_elements.add(bars, bar_labels, caption_panel)

        self.play(LaggedStart(*[GrowFromCenter(bar, run_time=1.0, rate_func=rate_functions.ease_out_expo) for bar in bars], lag_ratio=0.1))
        self.play(LaggedStart(*[bar.animate.set_fill(SECONDARY_ACCENT_COLOR, opacity=0.85) for bar in bars], lag_ratio=0.05, run_time=0.4, rate_func=rate_functions.linear))
        self.play(FadeIn(bar_labels, shift=UP*0.1, lag_ratio=0.1, run_time=0.6, rate_func=rate_functions.ease_out_sine))
        self.play(Write(caption_panel, run_time=1.0, rate_func=rate_functions.ease_out_sine))
        
        self.wait(15.0 - (1.0 + 0.4 + 0.6 + 1.0 + 0.5)) 
        self.play(FadeOut(scene4_elements, run_time=0.8, rate_func=rate_functions.ease_out_sine)) 
        self.wait(0.1)

        # --- SCENE 4: PERIOD FINDING (50s – 65s) ---
        scene5_elements = VGroup()
        axes_y_manim = -0.5 
        ax = Axes(
            x_range=[0, 7.5, 1], y_range=[-1, 15, 5],
            x_length=10, y_length=5,
            axis_config={"include_numbers": True, "font_size": 20, "color": TEXT_COLOR},
            tips=False, 
        ).move_to(UP * axes_y_manim)
        points_data = [(x, (2**x) % 15) for x in range(8)]
        graph_line = ax.plot(lambda x: (2**x) % 15, x_range=[0, 7, 0.05], color=GRAPH_COLOR, use_smoothing=True) 
        graph_vertices = VGroup(*[Dot(ax.c2p(x,y), color=PRIMARY_ACCENT_COLOR, radius=0.08) for x,y in points_data])
        moving_dot = Dot(ax.c2p(points_data[0][0], points_data[0][1]), color=ERROR_COLOR, radius=0.12)
        
        r_equals_4_text_pos = ax.c2p(2, 15.5) 
        
        def create_animated_dashed_line(x_val, y_top=15, y_bottom=-1):
            line = DashedLine(ax.c2p(x_val, y_bottom), ax.c2p(x_val, y_top), color=PRIMARY_ACCENT_COLOR, stroke_width=2.5, dash_length=0.2)
            return line

        dashed_line_0 = create_animated_dashed_line(0)
        dashed_line_4 = create_animated_dashed_line(4)
        scene5_elements.add(dashed_line_0, dashed_line_4)

        r_text = MathTex("r=4", font_size=36, color=TEXT_COLOR).move_to(r_equals_4_text_pos)
        r_text_panel = create_text_panel(r_text, padding=0.1)
        scene5_elements.add(ax, graph_line, graph_vertices, moving_dot, r_text_panel)

        if self.mobjects: 
            current_mobjects = self.mobjects.copy()
            if current_mobjects : self.play(FadeOut(*current_mobjects, run_time=0.5, rate_func=rate_functions.ease_out_sine))
        
        self.play(Create(ax, run_time=1.0, rate_func=rate_functions.ease_in_out_sine))
        self.play(Create(graph_line, run_time=1.2, rate_func=rate_functions.ease_in_out_sine), 
                  FadeIn(graph_vertices, lag_ratio=0.1, run_time=0.8, rate_func=rate_functions.ease_out_sine))
        self.add(moving_dot)
        dot_hop_animations = []
        for x_coord, y_coord in points_data: 
            dot_hop_animations.append(moving_dot.animate(run_time=0.55, rate_func=rate_functions.smooth).move_to(ax.c2p(x_coord, y_coord))) 
        self.play(Succession(*dot_hop_animations)) 
        
        self.play(Create(dashed_line_0, run_time=0.6, rate_func=rate_functions.ease_out_sine))
        self.play(Create(dashed_line_4, run_time=0.6, rate_func=rate_functions.ease_out_sine))
        self.play(Write(r_text_panel, run_time=0.6, rate_func=rate_functions.ease_out_sine))
        
        self.wait(15.0 - (0.5+1.0+1.2+0.8 + (0.55*len(points_data)) + 0.6+0.6+0.6 + 0.5)) 
        self.play(FadeOut(scene5_elements, run_time=0.5, rate_func=rate_functions.ease_out_sine))
        self.wait(0.1)

        # --- SCENE 5: QFT WAVE INTERFERENCE “AHA” (65s – 80s) ---
        scene6_elements = VGroup()
        wave_area_center_y = -1.0 
        axes_buff = 0.4

        wave_axes_height = 1.8 
        wave_x_range = [0, 8]
        axes_components = Axes(
            x_range=wave_x_range + [1], y_range=[-1.5, 1.5, 1],
            x_length=10, y_length=wave_axes_height * 1.2, 
            axis_config={"include_numbers": True, "font_size":20, "color": TEXT_COLOR}, 
            tips=False,
        ).move_to(UP * wave_axes_height * 0.6 + UP * wave_area_center_y) 
        scene6_elements.add(axes_components)
        
        axes_sum = Axes(
            x_range=wave_x_range + [1], y_range=[-3.5, 3.5, 1], 
            x_length=10, y_length=wave_axes_height, 
            axis_config={"include_numbers": True, "font_size":20, "color": TEXT_COLOR},
            tips=False,
        ).next_to(axes_components, DOWN, buff=axes_buff).align_to(axes_components, LEFT) 
        scene6_elements.add(axes_sum)
        
        time_tracker = ValueTracker(0) 
        speed = 0.6 * PI 
        k_period_4 = TAU / 4.0
        fx_amplitudes = [((2**i)%15)/15.0 * 0.7 + 0.3 for i in range(3)] 
        fx_phases = [PI/3.5 * ((2**i)%3.5) for i in range(3)] 

        def wave1_func(x): return fx_amplitudes[0] * np.sin(k_period_4 * x - speed * time_tracker.get_value() + fx_phases[0])
        def wave2_func(x): return fx_amplitudes[1] * np.sin(k_period_4 * x - speed * time_tracker.get_value() + fx_phases[1])
        def wave3_func(x): return fx_amplitudes[2] * np.sin(k_period_4 * x - speed * time_tracker.get_value() + fx_phases[2])
        def sum_wave_func(x): return wave1_func(x) + wave2_func(x) + wave3_func(x)
        
        plot_w1 = axes_components.plot(wave1_func, color=BLUE_C, use_smoothing=True, dt=0.01) 
        plot_w2 = axes_components.plot(wave2_func, color=TEAL_C, use_smoothing=True, dt=0.01)
        plot_w3 = axes_components.plot(wave3_func, color=GREEN_C, use_smoothing=True, dt=0.01) 
        plot_sum = axes_sum.plot(sum_wave_func, color=GRAPH_COLOR, stroke_width=4.5, use_smoothing=True, dt=0.01)
        
        plots_and_their_axes = [
            (plot_w1, wave1_func, axes_components),
            (plot_w2, wave2_func, axes_components),
            (plot_w3, wave3_func, axes_components),
            (plot_sum, sum_wave_func, axes_sum)
        ]
        for plot_obj, func_def, associated_axes_object in plots_and_their_axes:
            plot_obj.add_updater( # Corrected: dt is the second arg for the lambda
                lambda mob, dt, f=func_def, ax_obj=associated_axes_object: mob.become(
                    ax_obj.plot(f, color=mob.get_color(), stroke_width=mob.get_stroke_width(), use_smoothing=True, dt=0.01)
                )
            )
        scene6_elements.add(plot_w1, plot_w2, plot_w3, plot_sum)

        if self.mobjects:
            current_mobjects = self.mobjects.copy()
            if current_mobjects: self.play(FadeOut(*current_mobjects, run_time=0.5, rate_func=rate_functions.ease_out_sine))
            
        self.play(LaggedStart(
            Create(axes_components), Create(axes_sum),
            Create(plot_w1), Create(plot_w2), Create(plot_w3), Create(plot_sum),
            lag_ratio=0.1, run_time=1.2, rate_func=rate_functions.ease_in_out_sine)
        )
        
        self.play(time_tracker.animate(rate_func=rate_functions.smooth).set_value(4), run_time=4.0) 
        
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
        caption_qft.next_to(axes_components, UP, buff=0.3) 
        caption_qft_panel = create_text_panel(caption_qft, padding=0.15)
        scene6_elements.add(caption_qft_panel)
        self.play(Write(caption_qft_panel, run_time=0.8, rate_func=rate_functions.ease_out_sine))
        
        self.wait(15.0 - (0.5 + 1.2 + 4.0 + 0.4 + 0.4 + 0.8 + 0.5)) 
        for p_obj, _, _ in plots_and_their_axes: p_obj.clear_updaters() 
        self.play(FadeOut(scene6_elements, run_time=0.5, rate_func=rate_functions.ease_out_sine))
        self.wait(0.1)

        # --- SCENE 6: MEASURE & CALL TO ACTION (80s – 90s) ---
        scene7_elements = VGroup()
        
        if self.mobjects:
            current_mobjects = self.mobjects.copy()
            if current_mobjects: self.play(FadeOut(*current_mobjects, run_time=0.5, rate_func=rate_functions.ease_out_sine))

        k_text_str = "k = 2"
        k_text = Text(k_text_str, font_size=48, color=SECONDARY_ACCENT_COLOR)
        k_text_panel = create_text_panel(k_text.to_edge(UP, buff=1.0), padding=0.15, opacity=0.5, stroke_width=0)
        scene7_elements.add(k_text_panel)
        
        formula1_str = "r = 8 \\times 2^{-1} \\pmod 8 = 4"
        formula1 = MathTex(formula1_str, font_size=28, color=TEXT_COLOR)
        formula1_panel = create_text_panel(formula1.next_to(k_text_panel, DOWN, buff=0.4), padding=0.1, opacity=0.5, stroke_width=0)
        scene7_elements.add(formula1_panel)
        
        formula2_str = "\\gcd(2^{4/2}\\pm1, 15) \\rightarrow 3, 5"
        formula2 = MathTex(formula2_str, font_size=28, color=TEXT_COLOR) 
        formula2_panel = create_text_panel(formula2.next_to(formula1_panel, DOWN, buff=0.3), padding=0.1, opacity=0.5, stroke_width=0)
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
        cta1.next_to(formula2_panel, DOWN, buff=0.8) 
        scene7_elements.add(cta1) 

        cta2_str = "What secret will YOU unlock?"
        cta2 = Text(cta2_str, font_size=48, color=PRIMARY_ACCENT_COLOR, weight=BOLD)
        cta2.next_to(cta1, DOWN, buff=0.5) 
        scene7_elements.add(cta2)

        self.play(Write(cta1, run_time=0.8, rate_func=rate_functions.ease_out_sine))
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
        
        time_for_text_anims_s7 = 0.6 + 1.0 + 1.0 + (0.5*2+0.1) + 0.8 + 0.8 
        total_anim_time_budget_s7 = 9.5 
        
        wait_before_sparkles_start = total_anim_time_budget_s7 - time_for_text_anims_s7 - sparkle_duration
        if wait_before_sparkles_start < 0: wait_before_sparkles_start = 0.05

        self.wait(wait_before_sparkles_start)

        for _ in range(num_sparkles):
            sparkle_grey_shade = random.uniform(0.7, 1.0) 
            sparkle = Dot(radius=random.uniform(0.02, 0.05), 
                          color=rgb_to_color([sparkle_grey_shade, sparkle_grey_shade, sparkle_grey_shade]))
            sparkle.move_to([random.uniform(-config.frame_width/2.5, config.frame_width/2.5), 
                             random.uniform(cta2.get_bottom()[1] - 0.5, cta1.get_top()[1] + 0.5), 0]) 
            sparkles_group.add(sparkle) 
            sparkle_animations.append(Succession(
                FadeIn(sparkle, scale=0.5, run_time=random.uniform(0.3, 0.6)),
                FadeOut(sparkle, scale=0.5, run_time=random.uniform(0.3, 0.6))
            ))
        
        self.play(
            LaggedStart(*sparkle_animations, lag_ratio=(sparkle_duration / num_sparkles) * 0.6), 
            run_time=sparkle_duration
        )
        scene7_elements.add(sparkles_group) 
        
        # No Harvard Quantum Label here
        
        self.wait(0.1) # Buffer before final fade of this scene's elements

        self.play(FadeOut(scene7_elements, run_time=0.5, rate_func=rate_functions.ease_out_sine))
        self.wait(0.1) 

        # --- FINAL CREDITS SCREEN (New, separate, after 90s) ---
        credits_elements = VGroup()
        
        made_by_text = Text("Made by Dhaval Pandey, Tiffin School", font_size=36, color=TEXT_COLOR)
        made_by_text.center().shift(UP*0.3)
        
        read_desc_text = Text("Read description for more", font_size=28, color=PRIMARY_ACCENT_COLOR)
        read_desc_text.next_to(made_by_text, DOWN, buff=0.5)
        
        credits_elements.add(made_by_text, read_desc_text)
        
        # Ensure previous scene is fully cleared
        current_mobjects_before_credits = self.mobjects.copy()
        if current_mobjects_before_credits:
             self.play(FadeOut(*current_mobjects_before_credits, run_time=0.2))

        self.play(FadeIn(credits_elements, run_time=1.0, rate_func=rate_functions.ease_out_sine))
        self.wait(3.0) 
        self.play(FadeOut(credits_elements, run_time=1.0, rate_func=rate_functions.ease_in_sine))
        self.wait(0.5)