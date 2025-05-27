from manim import *
import random

# --- Style Configuration ---
DARK_BACKGROUND_COLOR = "#090d1a" 
TEXT_COLOR = WHITE
PRIMARY_ACCENT_COLOR = "#FFD700"  # Gold
SECONDARY_ACCENT_COLOR = "#38a3a5" # Teal
GRAPH_COLOR = "#00FF00"   # Bright Green for graphs
ERROR_COLOR = "#FF3333"   # Red
ICON_COLOR = WHITE

class QuantumEncryptionVideoEnhanced(Scene):
    def construct(self):
        self.camera.background_color = DARK_BACKGROUND_COLOR

        def create_text_panel(text_mobject, padding=0.1, opacity=0.60, bg_color=DARK_BACKGROUND_COLOR, stroke_color=PRIMARY_ACCENT_COLOR, stroke_width=0):
            panel_fill_color = bg_color
            # Simplified color check
            if bg_color == DARK_BACKGROUND_COLOR: 
                panel_fill_color = ManimColor(DARK_BACKGROUND_COLOR).interpolate(BLACK, 0.3)

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
        # Duration: 7s
        hook_elements = VGroup()
        
        icon_scale = 0.55
        email_icon = Text("✉", font_size=96, color=ICON_COLOR).scale(icon_scale)
        dollar_icon = Text("$", font_size=96, color=ICON_COLOR, weight=BOLD).scale(icon_scale)
        shield_icon = Text("🛡", font_size=96, color=ICON_COLOR).scale(icon_scale)
        
        icons = VGroup(email_icon, dollar_icon, shield_icon).arrange(RIGHT, buff=0.8).move_to(ORIGIN)
        hook_elements.add(icons)

        self.play(FadeIn(email_icon, run_time=0.5)) # 0.5
        self.wait(0.3) # 0.8
        self.play(FadeIn(dollar_icon, run_time=0.5)) # 1.3
        self.wait(0.3) # 1.6
        self.play(FadeIn(shield_icon, run_time=0.5)) # 2.1
        self.wait(0.2) # 2.3s
        
        number_2048 = Text("2048", font_size=280, color=TEXT_COLOR, weight=BOLD)
        number_2048.set_opacity(0.0)
        number_2048.move_to(ORIGIN).set_z_index(icons.z_index - 1)
        hook_elements.add(number_2048)

        lock_icon = Text("🔒", font_size=110, color=ERROR_COLOR)
        lock_icon.move_to(ORIGIN).set_z_index(number_2048.z_index + 1)
        hook_elements.add(lock_icon)

        self.play(
            number_2048.animate.set_opacity(0.25).scale(1.3, about_point=ORIGIN), run_time=1.5
        ) # 2.3 + 1.5 = 3.8s
        
        self.play(FadeIn(lock_icon, scale=0.5, run_time=0.3)) # 3.8 + 0.3 = 4.1s
        self.play(Indicate(lock_icon, scale_factor=1.2, color=RED_B, repetitions=2, run_time=0.6)) # 4.1 + 0.6 = 4.7s
        
        hook_text_str = "Or could quantum waves\nbreak every secret?" 
        hook_text_obj = Text(
            hook_text_str, font_size=48, color=TEXT_COLOR, weight=BOLD, line_spacing=0.9 
        ).move_to(ORIGIN) 
        hook_elements.add(hook_text_obj)
        
        self.play(
            FadeIn(hook_text_obj, shift=DOWN*0.1, run_time=1.0),
            FadeOut(icons, lock_icon, number_2048, run_time=0.8)
        ) # 4.7 + 1.0 = 5.7s
        
        self.wait(max(0.01, 7.0 - 5.7)) # Wait fills to 7.0s total for hook
        
        self.play(FadeOut(hook_text_obj, run_time=0.5)) 
        self.wait(0.1) # Transition buffer

        # --- SCENE 1: HISTORICAL TIMELINE (7s – 20s : 13s duration) ---
        # Duration: 13s
        scene2_elements = VGroup()
        timeline_y_pos = 0.5 
        timeline = Line(LEFT * 6, RIGHT * 6, color=PRIMARY_ACCENT_COLOR, stroke_width=3).move_to(UP * timeline_y_pos)
        scene2_elements.add(timeline)
        events_data = [
            (LEFT * 5, "1940·Turing", 0.0), (ORIGIN, "1977·RSA", 0.2), (RIGHT * 5, "1994·Shor", 0.4)
        ]
        markers_and_labels = VGroup()
        for x_pos_obj, text_str, delay in events_data:
            point_on_timeline = timeline.point_from_proportion( (x_pos_obj[0] - timeline.get_start()[0]) / timeline.get_length() if timeline.get_length() > 0 else 0.5 )
            dot = Dot(point=point_on_timeline, color=PRIMARY_ACCENT_COLOR, radius=0.1)
            label = Text(text_str, font_size=24, color=TEXT_COLOR).next_to(dot, DOWN, buff=0.35)
            markers_and_labels.add(VGroup(dot, label))
        scene2_elements.add(markers_and_labels)

        self.play(Create(timeline, run_time=0.8)) # 0.8s
        animation_sequence = []
        current_anim_time_s2 = 0.8 
        for i, event_group in enumerate(markers_and_labels):
            event_delay = events_data[i][2] 
            animation_sequence.append(Wait(event_delay))
            animation_sequence.append(FadeIn(event_group, shift=UP*0.2, run_time=0.5))
            current_anim_time_s2 += event_delay + 0.5
        self.play(Succession(*animation_sequence))
        
        self.wait(max(0.01, 13.0 - current_anim_time_s2 - 0.5)) # 0.5 for fade out
        self.play(FadeOut(scene2_elements, run_time=0.5))
        self.wait(0.1)

        # --- SCENE 2: CLASSICAL IMPOSSIBILITY (20s – 32s : 12s duration) ---
        # Duration: 12s
        scene3_elements = VGroup()
        original_bg_color_scene3 = self.camera.background_color 
        self.camera.background_color = "#222222" 

        n15_latex = MathTex("N = 15", font_size=64, color=TEXT_COLOR).to_edge(UP, buff=1.0)
        infinity_sym = Text("∞", font_size=90, color=ERROR_COLOR).next_to(n15_latex, DOWN, buff=0.8)
        caption_classical = Text("Classical ≈ infinite time", font_size=28, color=TEXT_COLOR).to_edge(DOWN, buff=1.2)
        scene3_elements.add(n15_latex, caption_classical, infinity_sym) 

        self.play(Write(n15_latex, run_time=1.0)) # 1.0s
        self.play(FadeIn(infinity_sym, run_time=0.5)) # 1.5s
        self.play(infinity_sym.animate(run_time=0.5, rate_func=rate_functions.wiggle).scale(1.1)) # 2.0s
        
        time_s3 = 2.0
        
        # Flash 1 ("Try 2x7") - Target display around 3.5s into scene
        self.wait(max(0.01, 3.5 - time_s3))
        time_s3 = 3.5
        flash1_text = Text("Try 2 × 7 = 14... ✕", font_size=30, color=ERROR_COLOR) 
        flash1_panel = create_text_panel(flash1_text.move_to(LEFT*3.5 + DOWN*0.5), padding=0.15, opacity=0.75)
        self.play(FadeIn(flash1_panel, run_time=0.2))
        self.wait(0.6) # Reduced hold
        self.play(FadeOut(flash1_panel, run_time=0.2))
        time_s3 += (0.2 + 0.6 + 0.2) # 1.0s for this flash -> time_s3 = 4.5s

        # Flash 2 ("Try 3x5") - Target display around 6.0s into scene
        self.wait(max(0.01, 6.0 - time_s3))
        time_s3 = 6.0
        flash2_text = Text("Try 3 × 5 = 15... ✓", font_size=30, color=GRAPH_COLOR) 
        flash2_panel = create_text_panel(flash2_text.move_to(RIGHT*3.5 + DOWN*0.5), padding=0.15, opacity=0.75)
        self.play(FadeIn(flash2_panel, run_time=0.2))
        self.wait(0.8) # Reduced hold
        self.play(FadeOut(flash2_panel, run_time=0.2))
        time_s3 += (0.2 + 0.8 + 0.2) # 1.2s for this flash -> time_s3 = 7.2s
        
        self.play(FadeIn(caption_classical, run_time=0.8)) # time_s3 = 8.0s
        time_s3 += 0.8
        
        infinity_growth_duration = 2.0 # Reduced growth duration
        self.play(infinity_sym.animate.scale(1.7).set_opacity(0.75).move_to(ORIGIN), run_time=infinity_growth_duration)
        time_s3 += infinity_growth_duration # time_s3 = 10.0s
            
        self.wait(max(0.01, 12.0 - time_s3 - 0.5)) # 0.5s for fade out
            
        self.play(FadeOut(scene3_elements, run_time=0.5))
        self.camera.background_color = original_bg_color_scene3 
        self.wait(0.1)

        # --- SCENE 3: SUPERPOSITION SPARK (32s – 44s : 12s duration) ---
        # Duration: 12s
        scene4_elements = VGroup()
        # ... (rest of mobject setup is fine)
        num_bars = 8; bar_area_center_y = 0.3; bar_height = 2.5
        bars = VGroup(*[Rectangle(width=0.7, height=bar_height, fill_color=TEXT_COLOR, fill_opacity=1, stroke_width=0) for _ in range(num_bars)]).arrange(RIGHT, buff=0.25).move_to(UP * bar_area_center_y)
        for bar in bars: bar.move_to(bar.get_bottom() + UP * bar_height / 2, aligned_edge=DOWN)
        bar_labels = VGroup(*[MathTex(f"|{i}\\rangle", font_size=28, color=TEXT_COLOR).next_to(bars[i], DOWN, buff=0.3) for i in range(num_bars)]).next_to(bars, DOWN, buff=0.4)
        caption_superposition = Text("Superposition = all states at once", font_size=32, color=PRIMARY_ACCENT_COLOR).to_edge(DOWN, buff=0.6)
        caption_panel = create_text_panel(caption_superposition, padding=0.15, opacity=0.75)
        scene4_elements.add(bars, bar_labels, caption_panel)

        anim_time_s4 = 1.0 + 0.4 + 0.6 + 1.0 # Bars, fill, labels, caption = 3.0s
        self.play(LaggedStart(*[GrowFromCenter(bar, run_time=1.0) for bar in bars], lag_ratio=0.1))
        self.play(LaggedStart(*[bar.animate.set_fill(SECONDARY_ACCENT_COLOR, opacity=0.85) for bar in bars], lag_ratio=0.05, run_time=0.4))
        self.play(FadeIn(bar_labels, shift=UP*0.1, lag_ratio=0.1, run_time=0.6))
        self.play(Write(caption_panel, run_time=1.0))
        
        self.wait(max(0.01, 12.0 - anim_time_s4 - 0.8)) # 0.8s for fade out
        self.play(FadeOut(scene4_elements, run_time=0.8)) 
        self.wait(0.1)

        # --- SCENE 4: PERIOD FINDING (44s – 59s : 15s duration) ---
        # Duration: 15s
        scene5_main_graph_elements = VGroup() 
        r_text_and_lines_group = VGroup() 
        # ... (rest of mobject setup is fine)
        axes_y_manim = -0.5 
        ax = Axes(x_range=[0, 7.5, 1], y_range=[-1, 15.5, 5], x_length=10, y_length=5.5, axis_config={"include_numbers": True, "font_size": 20, "color": TEXT_COLOR}, tips=False).move_to(UP * axes_y_manim)
        points_data = [(x, (2**x) % 15) for x in range(8)]
        graph_line = ax.plot(lambda x: (2**x) % 15, x_range=[0, 7.01, 0.01], color=GRAPH_COLOR, use_smoothing=False) 
        graph_vertices = VGroup(*[Dot(ax.c2p(x,y), color=PRIMARY_ACCENT_COLOR, radius=0.08) for x,y in points_data])
        moving_dot = Dot(ax.c2p(points_data[0][0], points_data[0][1]), color=ERROR_COLOR, radius=0.12)
        r_equals_4_text_pos = ax.c2p(2, ax.y_range[1] - 0.5) 
        def create_animated_dashed_line(x_val, y_top_coord=ax.y_range[1]-1, y_bottom_coord=ax.y_range[0]+0.5):
            return DashedLine(ax.c2p(x_val, y_bottom_coord), ax.c2p(x_val, y_top_coord), color=PRIMARY_ACCENT_COLOR, stroke_width=3, dash_length=0.25, dashed_ratio=0.6)
        dashed_line_0 = create_animated_dashed_line(0); dashed_line_4 = create_animated_dashed_line(4)
        r_text_and_lines_group.add(dashed_line_0, dashed_line_4)
        r_text_obj = MathTex("r=4", font_size=36, color=TEXT_COLOR).move_to(r_equals_4_text_pos)
        r_text_and_lines_group.add(r_text_obj) 
        scene5_main_graph_elements.add(ax, graph_line, graph_vertices, moving_dot)

        mobjects_to_clear_before_s5 = [m for m in self.mobjects]
        if mobjects_to_clear_before_s5: self.play(FadeOut(*mobjects_to_clear_before_s5, run_time=0.5))
        
        anim_time_s5 = 0.5 # initial fade
        self.play(Create(ax, run_time=1.0)); anim_time_s5 += 1.0
        self.play(Create(graph_line, run_time=1.2), FadeIn(graph_vertices, lag_ratio=0.1, run_time=0.8)); anim_time_s5 += 1.2 # Longest is 1.2
        self.add(moving_dot)
        
        dot_animation_total_time = 0
        for i in range(len(points_data)): 
            target_point = ax.c2p(points_data[i][0], points_data[i][1])
            hop_duration = 0.4 # Slowed down hop
            self.play(moving_dot.animate(run_time=hop_duration, rate_func=rate_functions.linear).move_to(target_point))
            dot_animation_total_time += hop_duration
        anim_time_s5 += dot_animation_total_time
        
        self.play(Create(dashed_line_0, run_time=0.7)); anim_time_s5 += 0.7
        self.play(Create(dashed_line_4, run_time=0.7)); anim_time_s5 += 0.7
        self.play(Write(r_text_obj, run_time=0.6)); anim_time_s5 += 0.6
        self.add(r_text_and_lines_group)

        self.wait(max(0.01, 15.0 - anim_time_s5 - 0.5)) # 0.5 for fadeout of main graph
        self.play(FadeOut(scene5_main_graph_elements, run_time=0.5))
        self.wait(0.1) 

        # --- SCENE 5: QFT WAVE INTERFERENCE “AHA” (59s – 72s : 13s duration) ---
        # Duration: 13s
        scene6_elements = VGroup()
        # ... (rest of mobject setup is fine)
        wave_area_center_y = -1.6; axes_buff = 0.35; wave_axes_height = 1.7; wave_x_range = [0, 8]
        axes_components = Axes(x_range=wave_x_range + [1], y_range=[-1.5, 1.5, 1], x_length=10, y_length=wave_axes_height * 1.2, axis_config={"include_numbers": True, "font_size":20, "color": TEXT_COLOR}, tips=False).move_to(UP * wave_axes_height * 0.6 + UP * wave_area_center_y)
        axes_sum = Axes(x_range=wave_x_range + [1], y_range=[-3.5, 3.5, 1], x_length=10, y_length=wave_axes_height, axis_config={"include_numbers": True, "font_size":20, "color": TEXT_COLOR}, tips=False).next_to(axes_components, DOWN, buff=axes_buff).align_to(axes_components, LEFT)
        scene6_elements.add(axes_components, axes_sum)
        time_tracker = ValueTracker(0); speed = 0.6 * PI; k_period_4 = TAU / 4.0
        fx_amplitudes = [((2**i)%15)/15.0 * 0.6 + 0.3 for i in range(3)]; fx_phases = [PI/3.0 * ((2**i)%3.0) for i in range(3)]
        def wave1_func(x): return fx_amplitudes[0] * np.sin(k_period_4 * x - speed * time_tracker.get_value() + fx_phases[0])
        def wave2_func(x): return fx_amplitudes[1] * np.sin(k_period_4 * x - speed * time_tracker.get_value() + fx_phases[1])
        def wave3_func(x): return fx_amplitudes[2] * np.sin(k_period_4 * x - speed * time_tracker.get_value() + fx_phases[2])
        def sum_wave_func(x): return wave1_func(x) + wave2_func(x) + wave3_func(x)
        plot_w1 = axes_components.plot(wave1_func, color=BLUE_C, use_smoothing=True, dt=0.005)
        plot_w2 = axes_components.plot(wave2_func, color=TEAL_C, use_smoothing=True, dt=0.005)
        plot_w3 = axes_components.plot(wave3_func, color=GREEN_C, use_smoothing=True, dt=0.005)
        plot_sum = axes_sum.plot(sum_wave_func, color=GRAPH_COLOR, stroke_width=4.5, use_smoothing=True, dt=0.005)
        plots_and_their_axes = [(plot_w1, wave1_func, axes_components), (plot_w2, wave2_func, axes_components), (plot_w3, wave3_func, axes_components), (plot_sum, sum_wave_func, axes_sum)]
        for plot_obj, func_def, associated_axes_object in plots_and_their_axes:
            plot_obj.add_updater(lambda mob, dt, f=func_def, ax_obj=associated_axes_object: mob.become(ax_obj.plot(f, color=mob.get_color(), stroke_width=mob.get_stroke_width(), use_smoothing=True, dt=0.005)))
        scene6_elements.add(plot_w1, plot_w2, plot_w3, plot_sum)

        mobjects_to_clear_before_s6 = [m for m in self.mobjects if m not in scene6_elements]
        if mobjects_to_clear_before_s6: self.play(FadeOut(*mobjects_to_clear_before_s6, run_time=0.5))
        
        anim_time_s6 = 0.5 # initial fade
        self.play(LaggedStart(Create(axes_components), Create(axes_sum), Create(plot_w1), Create(plot_w2), Create(plot_w3), Create(plot_sum), lag_ratio=0.1, run_time=1.2)); anim_time_s6 += 1.2
        self.play(time_tracker.animate(rate_func=linear).set_value(4), run_time=3.0); anim_time_s6 += 3.0 # Reduced wave travel
        
        x_peak_val = 4.0 
        if axes_sum.x_range[0] <= x_peak_val <= axes_sum.x_range[1]: # Pulse anim
            # ... (pulse animation code - approx 0.8s total)
            y_peak_val_sum = sum_wave_func(x_peak_val); peak_point_sum = axes_sum.c2p(x_peak_val, y_peak_val_sum)
            pulse_dot = Dot(peak_point_sum, color=PRIMARY_ACCENT_COLOR, radius=0.01); pulse_ring = Circle(radius=0.01, color=PRIMARY_ACCENT_COLOR, stroke_width=3).move_to(peak_point_sum)
            self.add(pulse_dot, pulse_ring) 
            self.play(Transform(pulse_dot, Dot(peak_point_sum, color=PRIMARY_ACCENT_COLOR, radius=0.15), run_time=0.4), Transform(pulse_ring, Circle(radius=0.3, color=PRIMARY_ACCENT_COLOR, stroke_width=4).move_to(peak_point_sum), run_time=0.4))
            self.play(FadeOut(pulse_dot, run_time=0.4), FadeOut(pulse_ring, run_time=0.4))
            anim_time_s6 += 0.8
            
        caption_qft = Text("QFT = Wave interference → period", font_size=32, color=TEXT_COLOR).next_to(axes_components, UP, buff=0.5)
        scene6_elements.add(caption_qft) 
        self.play(Write(caption_qft, run_time=0.8)); anim_time_s6 += 0.8
        
        self.wait(max(0.01, 13.0 - anim_time_s6 - 0.5)) # 0.5 for fade out
        for p_obj, _, _ in plots_and_their_axes: p_obj.clear_updaters() 
        self.play(FadeOut(scene6_elements, run_time=0.5))
        self.wait(0.1)

        # --- SCENE 6: MEASURE & CALL TO ACTION (72s – 82s : 10s duration) ---
        # Duration: 10s
        scene7_elements = VGroup()
        if self.mobjects: 
            current_mobjects = self.mobjects.copy()
            if current_mobjects: self.play(FadeOut(*current_mobjects, run_time=0.5))
        anim_time_s7 = 0.5 # initial fade

        k_text = Text("k = 2", font_size=48, color=SECONDARY_ACCENT_COLOR).to_edge(UP, buff=1.2)
        formula1 = MathTex("r = 8 \\times 2^{-1} \\pmod 8 = 4", font_size=30, color=TEXT_COLOR).next_to(k_text, DOWN, buff=0.5)
        formula2 = MathTex("\\gcd(2^{4/2}\\pm1, 15) \\rightarrow 3, 5", font_size=30, color=TEXT_COLOR).next_to(formula1, DOWN, buff=0.4)
        scene7_elements.add(k_text, formula1, formula2) 

        self.play(FadeIn(k_text, run_time=0.6)); anim_time_s7 += 0.6
        self.play(Write(formula1, run_time=1.0)); anim_time_s7 += 1.0
        self.play(Write(formula2, run_time=1.0)); anim_time_s7 += 1.0
        
        factor_3_highlight = formula2.get_part_by_tex("3").copy().set_color(GRAPH_COLOR)
        factor_5_highlight = formula2.get_part_by_tex("5").copy().set_color(GRAPH_COLOR)
        self.play(Succession(Indicate(factor_3_highlight, scale_factor=1.7, run_time=0.5), Wait(0.1), Indicate(factor_5_highlight, scale_factor=1.7, run_time=0.5))); anim_time_s7 += (0.5+0.1+0.5)
        
        cta1 = Text("Hidden rhythms shape our world.", font_size=36, color=TEXT_COLOR).next_to(formula2, DOWN, buff=0.8) 
        cta2 = Text("What secret will YOU unlock?", font_size=48, color=PRIMARY_ACCENT_COLOR, weight=BOLD).next_to(cta1, DOWN, buff=0.5) 
        scene7_elements.add(cta1, cta2)

        self.play(Write(cta1, run_time=0.8)); anim_time_s7 += 0.8
        cta2.scale(0.8)
        self.play(Write(cta2), cta2.animate.scale(1.25).set_rate_func(rate_functions.ease_out_bounce), run_time=0.8); anim_time_s7 += 0.8
        
        sparkle_duration = 2.0
        self.wait(max(0.01, 10.0 - anim_time_s7 - sparkle_duration - 0.5)) # 0.5s for final fadeout

        sparkles_group = VGroup()
        sparkle_animations = []
        num_sparkles = 15
        for _ in range(num_sparkles):
            sparkle_grey_shade = random.uniform(0.7, 1.0) 
            sparkle = Dot(radius=random.uniform(0.02, 0.05), color=rgb_to_color([sparkle_grey_shade]*3))
            sparkle.move_to([random.uniform(-config.frame_width/2.5, config.frame_width/2.5), random.uniform(cta2.get_bottom()[1] - 0.5, cta1.get_top()[1] + 0.5), 0]) 
            sparkles_group.add(sparkle) 
            sparkle_animations.append(Succession(FadeIn(sparkle, scale=0.5, run_time=random.uniform(0.3, 0.6)), FadeOut(sparkle, scale=0.5, run_time=random.uniform(0.3, 0.6))))
        self.play(LaggedStart(*sparkle_animations, lag_ratio=(sparkle_duration / num_sparkles) * 0.6), run_time=sparkle_duration)
        scene7_elements.add(sparkles_group) 
                
        self.wait(0.1) 
        self.play(FadeOut(scene7_elements, run_time=0.5))
        self.wait(0.1) 

        # --- FINAL CREDITS SCREEN (82s – 86s : 4s duration) ---
        # Duration: 1s FadeIn + 2s Hold + 1s FadeOut = 4s
        credits_elements = VGroup()
        made_by_text = Text("Made by Dhaval Pandey, Tiffin School", font_size=36, color=TEXT_COLOR).center().shift(UP*0.3)
        read_desc_text = Text("Read description for more", font_size=28, color=PRIMARY_ACCENT_COLOR).next_to(made_by_text, DOWN, buff=0.5)
        credits_elements.add(made_by_text, read_desc_text)
        
        current_mobjects_before_credits = self.mobjects.copy()
        if current_mobjects_before_credits: self.play(FadeOut(*current_mobjects_before_credits, run_time=0.2))

        self.play(FadeIn(credits_elements, run_time=1.0))
        self.wait(2.0) # User requested 2s hold
        self.play(FadeOut(credits_elements, run_time=1.0))
        self.wait(0.5) # Final pause