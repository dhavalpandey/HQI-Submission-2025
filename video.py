from manim import *
import random
import numpy as np
from scipy.interpolate import CubicSpline

DARK_BACKGROUND_COLOR = "#090d1a"
TEXT_COLOR = WHITE
PRIMARY_ACCENT_COLOR = "#FFD700"
SECONDARY_ACCENT_COLOR = "#38a3a5"
GRAPH_COLOR = "#00FF00"
ERROR_COLOR = "#FF3333"
ICON_COLOR = WHITE

def create_title(text_str):
    return Text(text_str, font_size=40, color=PRIMARY_ACCENT_COLOR).to_edge(UP, buff=0.5)

class QuantumBaseScene(Scene):
    def setup_scene_defaults(self):
        self.camera.background_color = DARK_BACKGROUND_COLOR

class IntroScenes(QuantumBaseScene):
    def construct(self):
        self.setup_scene_defaults()

        current_scene_duration_target_s0 = 7.0; anim_time_s0 = 0
        hook_elements = VGroup()
        icon_scale = 0.55
        email_icon = Text("✉", font_size=96, color=ICON_COLOR).scale(icon_scale)
        dollar_icon = Text("$", font_size=96, color=ICON_COLOR, weight=BOLD).scale(icon_scale)
        shield_icon = Text("🛡", font_size=96, color=ICON_COLOR).scale(icon_scale)
        icons = VGroup(email_icon, dollar_icon, shield_icon).arrange(RIGHT, buff=0.8).move_to(ORIGIN)
        hook_elements.add(icons)
        self.play(FadeIn(email_icon, run_time=0.5)); anim_time_s0 += 0.5
        self.wait(0.3); anim_time_s0 += 0.3
        self.play(FadeIn(dollar_icon, run_time=0.5)); anim_time_s0 += 0.5
        self.wait(0.3); anim_time_s0 += 0.3
        self.play(FadeIn(shield_icon, run_time=0.5)); anim_time_s0 += 0.5
        self.wait(0.2); anim_time_s0 += 0.2
        number_2048 = Text("2048", font_size=280, color=TEXT_COLOR, weight=BOLD).set_opacity(0.0).move_to(ORIGIN).set_z_index(icons.z_index - 1)
        hook_elements.add(number_2048)
        lock_icon_s0 = Text("🔒", font_size=110, color=ERROR_COLOR).move_to(ORIGIN).set_z_index(number_2048.z_index + 1)
        hook_elements.add(lock_icon_s0)
        self.play(number_2048.animate.set_opacity(0.25).scale(1.3, about_point=ORIGIN), run_time=1.5); anim_time_s0 += 1.5
        self.play(FadeIn(lock_icon_s0, scale=0.5, run_time=0.3)); anim_time_s0 += 0.3
        self.play(Indicate(lock_icon_s0, scale_factor=1.2, color=RED_B, repetitions=2, run_time=0.6)); anim_time_s0 += 0.6
        hook_text_str = "Or could quantum waves\nbreak every secret?"
        hook_text_obj = Text(hook_text_str, font_size=48, color=TEXT_COLOR, weight=BOLD, line_spacing=0.9).move_to(ORIGIN)
        hook_elements.add(hook_text_obj)
        self.play(FadeIn(hook_text_obj, shift=DOWN*0.1, run_time=1.0), FadeOut(icons, lock_icon_s0, number_2048, run_time=0.8)); anim_time_s0 += 1.0
        self.wait(max(0.01, current_scene_duration_target_s0 - anim_time_s0 - 0.5))
        self.play(FadeOut(hook_elements, run_time=0.5))
        self.wait(0.1)

        current_scene_duration_target_s1 = 13.0; anim_time_s1 = 0
        scene1_elements = VGroup()
        timeline_y_pos = 0.5
        timeline = Line(LEFT * 6, RIGHT * 6, color=PRIMARY_ACCENT_COLOR, stroke_width=3).move_to(UP * timeline_y_pos)
        scene1_elements.add(timeline)
        events_data = [(LEFT * 5, "1940s · Turing", 0.0), (ORIGIN, "1977 · RSA", 0.2), (RIGHT * 5, "1994 · Shor", 0.4)]
        markers_and_labels = VGroup()
        for x_pos_obj, text_str, delay in events_data:
            point_on_timeline = timeline.point_from_proportion((x_pos_obj[0] - timeline.get_start()[0]) / timeline.get_length() if timeline.get_length() > 0 else 0.5)
            dot = Dot(point=point_on_timeline, color=PRIMARY_ACCENT_COLOR, radius=0.1)
            label = Text(text_str, font_size=24, color=TEXT_COLOR).next_to(dot, DOWN, buff=0.35)
            markers_and_labels.add(VGroup(dot, label))
        scene1_elements.add(markers_and_labels)
        self.play(Create(timeline, run_time=0.8)); anim_time_s1 += 0.8
        animation_sequence = []
        for i, event_group in enumerate(markers_and_labels):
            event_delay = events_data[i][2]
            animation_sequence.append(Wait(event_delay))
            animation_sequence.append(FadeIn(event_group, shift=UP*0.2, run_time=0.5))
            anim_time_s1 += event_delay + 0.5
        self.play(Succession(*animation_sequence))
        self.wait(max(0.01, current_scene_duration_target_s1 - anim_time_s1 - 0.5))
        self.play(FadeOut(scene1_elements, run_time=0.5))
        self.wait(0.1)

        current_scene_duration_target_s2 = 13.0; anim_time_s2 = 0
        scene2_elements = VGroup()
        original_bg_color_scene2 = self.camera.background_color
        self.camera.background_color = ManimColor("#1A1A1A")

        n15_latex = MathTex("N = 15", font_size=72, color=TEXT_COLOR).to_edge(UP, buff=1.0)
        infinity_sym = Text("∞", font_size=100, color=ERROR_COLOR).next_to(n15_latex, DOWN, buff=0.8)
        caption_classical = Text("Classical computers: Too slow for big numbers!", font_size=28, color=TEXT_COLOR).to_edge(DOWN, buff=1.2)
        scene2_elements.add(n15_latex, caption_classical, infinity_sym)
        self.play(Write(n15_latex, run_time=1.0)); anim_time_s2 += 1.0
        self.play(FadeIn(infinity_sym, run_time=0.5)); anim_time_s2 += 0.5
        self.play(infinity_sym.animate(run_time=0.5, rate_func=rate_functions.wiggle).scale(1.1)); anim_time_s2 += 0.5

        def create_flash_panel(text_str, color, position):
            text_mobj = Text(text_str, font_size=36, color=color)
            panel_fill_color = ManimColor("#1A1A1A").interpolate(BLACK, 0.5)
            panel = Rectangle(
                width=text_mobj.width + 0.4, height=text_mobj.height + 0.4,
                fill_color=panel_fill_color, fill_opacity=0.8, stroke_width=0
            ).move_to(text_mobj.get_center())
            return VGroup(panel, text_mobj).move_to(position)

        flash_start_time = anim_time_s2 + 0.5
        flash1_panel = create_flash_panel("Try 2 × 7 = 14... ✕", ERROR_COLOR, LEFT*3.5 + DOWN*0.5)
        self.wait(max(0.01, flash_start_time - anim_time_s2))
        anim_time_s2 = flash_start_time
        self.play(FadeIn(flash1_panel, run_time=0.2)); anim_time_s2 += 0.2
        self.wait(1.5); anim_time_s2 += 1.5
        self.play(FadeOut(flash1_panel, run_time=0.2)); anim_time_s2 += 0.2

        flash2_start_time = anim_time_s2 + 1.0
        flash2_panel = create_flash_panel("Try 3 × 5 = 15... ✓", GRAPH_COLOR, RIGHT*3.5 + DOWN*0.5)
        self.wait(max(0.01, flash2_start_time - anim_time_s2))
        anim_time_s2 = flash2_start_time
        self.play(FadeIn(flash2_panel, run_time=0.2)); anim_time_s2 += 0.2
        self.wait(1.5); anim_time_s2 += 1.5
        self.play(FadeOut(flash2_panel, run_time=0.2)); anim_time_s2 += 0.2

        self.play(FadeIn(caption_classical, run_time=0.8)); anim_time_s2 += 0.8
        infinity_growth_duration = 2.0
        self.play(infinity_sym.animate.scale(1.7).set_opacity(0.75).move_to(ORIGIN), run_time=infinity_growth_duration)
        anim_time_s2 += infinity_growth_duration
        self.wait(max(0.01, current_scene_duration_target_s2 - anim_time_s2 - 0.5))
        self.play(FadeOut(scene2_elements, run_time=0.5))
        self.camera.background_color = DARK_BACKGROUND_COLOR
        self.wait(0.1)

class PeriodFindingAndSuperposition(QuantumBaseScene):
    def construct(self):
        self.setup_scene_defaults()

        current_scene_duration_s1 = 18.0; anim_time_s1 = 0
        scene1_elements = VGroup()
        title_s1 = create_title("Shor's Algorithm: Finding the Secret Rhythm")
        scene1_elements.add(title_s1)
        self.play(Write(title_s1, run_time=0.8)); anim_time_s1 += 0.8

        N_val = 15
        a_val = 2

        n_a_text_group = VGroup(
            MathTex(f"N = {N_val}", font_size=32),
            MathTex(f"\\text{{Our guess: }} a = {a_val}", font_size=32)
        ).arrange(RIGHT, buff=1.0).next_to(title_s1, DOWN, buff=0.45)
        scene1_elements.add(n_a_text_group)

        self.play(Write(n_a_text_group[0]), run_time=0.7); anim_time_s1 += 0.7
        self.wait(0.5); anim_time_s1 += 0.5
        self.play(Write(n_a_text_group[1]), run_time=0.7); anim_time_s1 += 0.7
        self.wait(0.8); anim_time_s1 += 0.8

        calc_display_s1 = MathTex("", font_size=28, color=YELLOW_A).to_edge(DOWN, buff=0.3)
        scene1_elements.add(calc_display_s1)

        wheel_radius = 2.0
        wheel_center = ORIGIN + DOWN * 0.4
        number_wheel = Circle(radius=wheel_radius, color=SECONDARY_ACCENT_COLOR, stroke_width=5).move_to(wheel_center)
        wheel_ticks_labels = VGroup()
        for i in range(N_val):
            angle = TAU * i / N_val - PI/2
            pos = wheel_center + wheel_radius * np.array([np.cos(angle), np.sin(angle), 0])
            label_pos = pos + 0.28 * np.array([np.cos(angle), np.sin(angle), 0])
            label = Text(str(i), font_size=16).move_to(label_pos)
            wheel_ticks_labels.add(label)

        scene1_elements.add(number_wheel, wheel_ticks_labels)
        self.play(Create(number_wheel), FadeIn(wheel_ticks_labels, lag_ratio=0.05), run_time=1.0); anim_time_s1 += 1.0

        live_sequence_display = VGroup().move_to(wheel_center)
        scene1_elements.add(live_sequence_display)
        landing_spots_highlights = VGroup().set_z_index(1)
        scene1_elements.add(landing_spots_highlights)

        current_val = 1
        pulse = Dot(radius=0.12, color=PRIMARY_ACCENT_COLOR)
        pulse_aura = Dot(radius=0.12, color=PRIMARY_ACCENT_COLOR, fill_opacity=0.3).scale(2.0)
        pulse_group = VGroup(pulse, pulse_aura).set_z_index(10).move_to(number_wheel.get_top())

        max_x = 7
        r_val = 0
        anim_calc_write = 0.4
        anim_pulse_move = 0.65
        anim_spot_write = 0.55

        for x_val in range(max_x + 1):
            new_calc_str = f"\\text{{Step }} {x_val}: {a_val}^{{{x_val}}} \\pmod{{{N_val}}} = {current_val}"
            new_calc_display = MathTex(new_calc_str, font_size=28, color=YELLOW_A).move_to(calc_display_s1.get_center())

            angle = TAU * current_val / N_val - PI/2
            target_pos_on_wheel = wheel_center + wheel_radius * np.array([np.cos(angle), np.sin(angle), 0])

            if x_val == 0:
                pulse_group.move_to(target_pos_on_wheel)
                self.play(Transform(calc_display_s1, new_calc_display), GrowFromCenter(pulse_group), run_time=max(anim_calc_write, anim_pulse_move))
            else:
                self.play(Transform(calc_display_s1, new_calc_display), pulse_group.animate.move_to(target_pos_on_wheel), run_time=max(anim_calc_write, anim_pulse_move), rate_func=rate_functions.ease_in_out_sine)
            anim_time_s1 += max(anim_calc_write, anim_pulse_move)

            landing_spot_highlight = Dot(point=target_pos_on_wheel, radius=0.2, color=GRAPH_COLOR, fill_opacity=0.4).set_z_index(landing_spots_highlights.z_index)
            landing_spots_highlights.add(landing_spot_highlight)

            val_text = MathTex(str(current_val), font_size=26, color=GRAPH_COLOR)
            live_sequence_display.add(val_text)

            self.play(
                GrowFromCenter(landing_spot_highlight),
                live_sequence_display.animate.arrange(RIGHT, buff=0.22).move_to(wheel_center),
                run_time=anim_spot_write
            )
            anim_time_s1 += anim_spot_write

            if x_val == 3: r_val = 4
            if x_val < max_x: current_val = (a_val**(x_val+1)) % N_val

        self.play(FadeOut(calc_display_s1), run_time=0.2); anim_time_s1 += 0.2

        period_explanation_group = VGroup()
        if r_val > 0 and len(live_sequence_display) >= r_val:
            first_r_values_in_seq = VGroup(*live_sequence_display[0:r_val])
            period_underline = Underline(
                first_r_values_in_seq,
                color=PRIMARY_ACCENT_COLOR,
                stroke_width=3,
                buff=0.15
            )
            length_text = MathTex(
                f"\\text{{Pattern length: }} r = {r_val}",
                font_size=26,
                color=PRIMARY_ACCENT_COLOR
            )
            length_text.next_to(period_underline, DOWN, buff=0.2)
            length_text.set_x(wheel_center[0])
            period_explanation_group.add(period_underline, length_text)

        scene1_elements.add(period_explanation_group)
        self.play(Write(period_explanation_group), run_time=1.3); anim_time_s1 += 1.3
        self.wait(1.0); anim_time_s1 += 1.0

        self.wait(max(0.01, current_scene_duration_s1 - anim_time_s1 - 0.5))
        elements_to_fade_s1 = VGroup(scene1_elements, pulse_group, landing_spots_highlights, live_sequence_display)
        self.play(FadeOut(elements_to_fade_s1), run_time=0.5)
        self.wait(0.1)

        current_scene_duration_s2 = 10.0; anim_time_s2 = 0
        scene2_elements = VGroup()
        title_s2 = create_title("Superposition: The Quantum Magic")
        scene2_elements.add(title_s2)
        self.play(Write(title_s2, run_time=0.7)); anim_time_s2 += 0.7

        classical_label = Text("Classical Bit:", font_size=28, color=TEXT_COLOR).move_to(LEFT*4.0 + UP*1.8)
        bit_0_visual = Circle(radius=0.4, color=BLUE_D, fill_opacity=0.7).next_to(classical_label, DOWN, buff=0.35)
        text_0_cb = Text("0", font_size=32, color=TEXT_COLOR).move_to(bit_0_visual)
        bit_1_visual = Circle(radius=0.4, color=GREEN_D, fill_opacity=0.7).move_to(bit_0_visual)
        text_1_cb = Text("1", font_size=32, color=TEXT_COLOR).move_to(bit_1_visual)
        classical_desc = Text("One state at a time", font_size=22, color=TEXT_COLOR).next_to(bit_0_visual, DOWN, buff=0.5)
        classical_group = VGroup(classical_label, bit_0_visual, text_0_cb, classical_desc)
        scene2_elements.add(classical_group)
        self.play(FadeIn(classical_group, shift=RIGHT*0.2), run_time=0.7); anim_time_s2 += 0.7

        outer_pulse_0 = Circle(radius=0.4, color=BLUE_E, stroke_width=6).move_to(bit_0_visual)
        outer_pulse_1 = Circle(radius=0.4, color=GREEN_E, stroke_width=6).move_to(bit_1_visual)
        self.play(
            Transform(VGroup(bit_0_visual, text_0_cb), VGroup(bit_1_visual, text_1_cb)),
            Succession(
                Transform(outer_pulse_0, outer_pulse_0.copy().scale(1.6).set_opacity(0), rate_func=rate_functions.ease_out_sine),
                Wait(0.05),
                Transform(outer_pulse_1, outer_pulse_1.copy().scale(1.6).set_opacity(0), rate_func=rate_functions.ease_out_sine, remover=True),
            ),
            rate_func=rate_functions.there_and_back_with_pause, run_time=1.5
        ); anim_time_s2 += 1.5; self.remove(outer_pulse_0, outer_pulse_1)

        qubit_label = Text("Quantum Bit (Qubit):", font_size=28, color=TEXT_COLOR).move_to(RIGHT*4.0 + UP*1.8)
        sphere_center = qubit_label.get_center() + DOWN*2.0; radius = 1.1
        ghost_sphere = Sphere(radius=radius, resolution=(20,20), fill_opacity=0.15, stroke_opacity=0.25, color=GRAY)
        ghost_sphere.move_to(sphere_center)
        pole_0 = sphere_center + UP * radius; pole_1 = sphere_center + DOWN * radius
        label_0_s2 = MathTex("|0\\rangle", font_size=34).next_to(pole_0, UP, buff=0.1)
        label_1_s2 = MathTex("|1\\rangle", font_size=34).next_to(pole_1, DOWN, buff=0.1)
        z_axis = DashedLine(pole_0, pole_1, dash_length=0.1, color=GRAY, stroke_width=2.5)
        qubit_arrow = Arrow(start=sphere_center, end=sphere_center + UP*radius*0.8, color=PRIMARY_ACCENT_COLOR, buff=0, stroke_width=6, max_tip_length_to_length_ratio=0.18)
        qubit_desc = Text("Multiple states at a time!", font_size=22, color=TEXT_COLOR).next_to(ghost_sphere, DOWN, buff=0.7)

        qubit_viz_group = VGroup(qubit_label, ghost_sphere, z_axis, label_0_s2, label_1_s2, qubit_arrow, qubit_desc)
        scene2_elements.add(qubit_viz_group)
        self.play(FadeIn(qubit_viz_group, shift=LEFT*0.2), run_time=0.8); anim_time_s2 += 0.8

        path_func_s2 = lambda t: sphere_center + radius * np.array([ np.sin(TAU*t*1.2+PI/3)*np.cos(TAU*t*0.9+PI/4), np.sin(TAU*t*1.2+PI/3)*np.sin(TAU*t*0.9+PI/4), np.cos(TAU*t*1.2+PI/3) ])
        path_s2 = ParametricFunction(path_func_s2, t_range=[0,1.5], stroke_width=0)
        arrow_tip_tracker = Dot(point=path_s2.get_start(), radius=0.001).set_opacity(0)
        qubit_arrow.add_updater(lambda mob: mob.put_start_and_end_on(sphere_center, arrow_tip_tracker.get_center()))
        trail = TracedPath(arrow_tip_tracker.get_center, stroke_color=PRIMARY_ACCENT_COLOR, stroke_width=3, stroke_opacity=[0,0.6,0], dissipating_time=0.4)
        self.add(arrow_tip_tracker, qubit_arrow, trail)
        self.play(ghost_sphere.animate.set_fill(opacity=0.25).set_stroke(opacity=0.4), MoveAlongPath(arrow_tip_tracker, path_s2), run_time=3.5); anim_time_s2 += 3.5
        qubit_arrow.clear_updaters(); self.remove(trail)

        self.wait(max(0.01, current_scene_duration_s2 - anim_time_s2 - 0.5))
        self.play(FadeOut(scene2_elements, run_time=0.5))
        self.wait(0.1)

class QFTPeriodFindingScene(QuantumBaseScene):
    """
    A final, polished, 20-second animation of the QFT process with refined
    visuals and pacing for a clear and engaging narrative.
    """
    def construct(self):
        self.setup_scene_defaults()

        N = 15
        a = 2
        r = 4
        LABEL_FONT_SIZE = 24

        title = create_title("QFT: How Quantum Finds Patterns")
        self.play(Write(title), run_time=1.0)

        input_axes = Axes(
            x_range=[0, 16, 4], y_range=[-2, 16, 5], x_length=10, y_length=4.0,
            axis_config={"include_numbers": True, "font_size": 24, "color": TEXT_COLOR},
            tips=False,
        ).next_to(title, DOWN, buff=0.5)

        x_label = input_axes.get_x_axis_label(Text("x (inputs)", font_size=LABEL_FONT_SIZE), edge=DOWN, buff=1.2)
        y_label = MathTex("2^x \\pmod{15}", font_size=LABEL_FONT_SIZE).rotate(PI/2).next_to(input_axes.y_axis, LEFT, buff=0.4)
        input_axes.add(x_label, y_label)

        x_coords = np.arange(0, 17); y_coords = (a**x_coords) % N
        spline = CubicSpline(x_coords, y_coords, bc_type='periodic')
        graph_line = input_axes.plot(spline, x_range=[0, 16], color=GRAPH_COLOR, stroke_width=4)
        graph_dots = VGroup(*[Dot(input_axes.c2p(x, y), color=PRIMARY_ACCENT_COLOR, radius=0.07) for x, y in zip(x_coords[:-1], y_coords[:-1])])

        self.play(Create(input_axes), Create(graph_line), FadeIn(graph_dots, lag_ratio=0.05), run_time=2.0)
        self.wait(1.0)

        input_visuals = VGroup(input_axes, graph_line, graph_dots)
        self.play(FadeOut(title), input_visuals.animate.scale(0.35).to_edge(UP, buff=0.25), run_time=1.0)

        qft_box = RoundedRectangle(height=2.5, width=3.0, corner_radius=0.2, color=SECONDARY_ACCENT_COLOR, fill_opacity=0.15).next_to(input_visuals, DOWN, buff=0.5)
        qft_label = Text("QFT", font_size=24, weight=BOLD).move_to(qft_box)
        qft_processor = VGroup(qft_box, qft_label)

        self.play(FadeIn(qft_processor), run_time=0.5)
        self.play(input_visuals.animate.move_to(qft_box.get_center()).scale(0.01), run_time=1.0)
        self.remove(input_visuals)

        center_proc = qft_processor.get_center()
        qft_waves = VGroup()
        for _ in range(15):
            wave = ParametricFunction(
                lambda t: np.array([t, 0.2*np.sin(random.uniform(3,6)*t + random.uniform(0,TAU)), 0]),
                t_range=[-1.0, 1.0], stroke_width=random.uniform(1.5, 2.5),
                color=interpolate_color(ManimColor(SECONDARY_ACCENT_COLOR), ManimColor(PRIMARY_ACCENT_COLOR), random.random())
            ).scale(random.uniform(0.5, 0.8)).move_to(center_proc).rotate(random.uniform(0, TAU))
            qft_waves.add(wave)

        self.play(LaggedStart(*[Create(w) for w in qft_waves], lag_ratio=0.1), run_time=1.0)

        for i in range(4):
            rt = 0.5 - i * 0.1
            scale_factor = 1.1 + i * 0.2
            wiggle_intensity = 1.05 + i * 0.05
            rotation_anims = [Rotate(wave, angle=TAU * 0.5 * random.choice([-1, 1]), rate_func=linear) for wave in qft_waves]

            self.play(
                AnimationGroup(*rotation_anims),
                qft_processor.animate.scale(scale_factor),
                Wiggle(qft_processor, scale_value=wiggle_intensity, rotation_angle=0.03 * (i+1) * TAU),
                run_time=rt
            )

        self.play(FadeOut(qft_processor, scale=5), FadeOut(qft_waves), Flash(center_proc, color=PRIMARY_ACCENT_COLOR, line_length=1.0, num_lines=20, flash_radius=3.5), run_time=0.5)

        period_result = MathTex("r = 4", font_size=72, color=PRIMARY_ACCENT_COLOR)
        self.play(Write(period_result), run_time=1.0)

        self.play(period_result.animate.to_edge(UP, buff=1.0), run_time=1.0)

        known_values = VGroup(
            MathTex("a = 2", font_size=48),
            MathTex("N = 15", font_size=48)
        ).arrange(RIGHT, buff=1.0).next_to(period_result, DOWN, buff=0.75)
        self.play(FadeIn(known_values, lag_ratio=0.5), run_time=1.0)

        calc_group = VGroup(
            MathTex("gcd(a^{r/2} - 1, N)"),
            MathTex("gcd(a^{r/2} + 1, N)")
        ).arrange(RIGHT, buff=2.0).next_to(known_values, DOWN, buff=1.0).scale(0.9)
        self.play(Write(calc_group), run_time=1.0)

        sub_group = VGroup(
            MathTex("gcd(2^{4/2} - 1, 15)"),
            MathTex("gcd(2^{4/2} + 1, 15)")
        ).arrange(RIGHT, buff=2.0).move_to(calc_group)
        self.play(Transform(calc_group, sub_group), run_time=1.0)

        eval_group = VGroup(
            MathTex("gcd(3, 15)"),
            MathTex("gcd(5, 15)")
        ).arrange(RIGHT, buff=3.0).move_to(calc_group)
        self.play(Transform(calc_group, eval_group), run_time=1.0)

        final_factors = VGroup(
            MathTex("3", font_size=72, color=GRAPH_COLOR),
            MathTex("5", font_size=72, color=GRAPH_COLOR)
        ).arrange(RIGHT, buff=4.0).move_to(calc_group)

        boxes = VGroup(
            SurroundingRectangle(final_factors[0], color=GRAPH_COLOR, buff=0.2),
            SurroundingRectangle(final_factors[1], color=GRAPH_COLOR, buff=0.2)
        )

        self.play(Transform(calc_group, final_factors), Create(boxes), run_time=1.5)

        conclusion = Text("Prime factors found!", font_size=36, color=PRIMARY_ACCENT_COLOR).next_to(boxes, DOWN, buff=1.0)
        self.play(Write(conclusion), run_time=1.0)

        self.wait(1.0)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

class OutroScene(QuantumBaseScene):
    def construct(self):
        self.setup_scene_defaults()

        current_scene_duration_cta = 5.0; anim_time_cta = 0
        cta_elements = VGroup()

        cta1 = Text("Shor's algorithm uses embedded patterns,", font_size=36, color=TEXT_COLOR, t2w={'hidden patterns': BOLD}).move_to(UP*0.8)
        cta2 = Text("hidden deep within waves.", font_size=36, color=TEXT_COLOR, t2w={'great challenges': BOLD}).next_to(cta1, DOWN, buff=0.3)
        cta3 = Text("And this can all be unlocked using quantum.", font_size=48, color=PRIMARY_ACCENT_COLOR, weight=BOLD).next_to(cta2, DOWN, buff=0.8)
        cta_elements.add(cta1, cta2, cta3)

        self.play(Write(cta1, rate_func=slow_into), run_time=1.0); anim_time_cta += 1.0
        self.play(Write(cta2, rate_func=slow_into), run_time=1.0); anim_time_cta += 1.0
        self.play(GrowFromCenter(cta3, rate_func=rate_functions.ease_out_elastic), run_time=1.2); anim_time_cta += 1.2

        sparkle_duration = 1.3
        sparkle_anims_cta = []
        for _ in range(35):
            sparkle = Dot(radius=random.uniform(0.005, 0.035)).set_color(random_bright_color())
            sparkle.set_opacity(random.uniform(0.6, 1.0))
            start_pos = cta3.get_center()
            end_pos = start_pos + rotate_vector(RIGHT * random.uniform(1.8, config.frame_width/2.0), random.uniform(0, TAU))
            sparkle.move_to(start_pos)
            sparkle_anims_cta.append(
                sparkle.animate(
                    path_arc=random.uniform(-PI/2.5, PI/2.5),
                    rate_func=rate_functions.rush_from if random.random() > 0.5 else rate_functions.rush_into
                ).move_to(end_pos).set_opacity(0).scale(random.uniform(0.5,1.2))
            )
        self.play(LaggedStart(*sparkle_anims_cta, lag_ratio=0.015, run_time=sparkle_duration)); anim_time_cta += sparkle_duration

        self.wait(max(0.01, current_scene_duration_cta - anim_time_cta - 0.5))
        self.play(FadeOut(cta_elements, run_time=0.5))
        self.wait(0.1)

        current_scene_duration_credits = 5.0; anim_time_credits = 0
        credits_elements = VGroup()
        code_by_text = Text("Code by Dhaval Pandey, Tiffin School", font_size=36, color=TEXT_COLOR).center().shift(UP*0.3)
        contest_text = Text("Read description for more", font_size=28, color=PRIMARY_ACCENT_COLOR).next_to(code_by_text, DOWN, buff=0.5)
        credits_elements.add(code_by_text, contest_text)

        self.play(FadeIn(credits_elements, run_time=1.0)); anim_time_credits += 1.0
        self.wait(max(0.01, current_scene_duration_credits - anim_time_credits - 1.0))
        self.play(FadeOut(credits_elements, run_time=1.0))
        self.wait(0.1)

class FullVideo(QuantumBaseScene):
    def construct(self):
        self.setup_scene_defaults()
        IntroScenes.construct(self)
        PeriodFindingAndSuperposition.construct(self)
        QFTPeriodFindingScene.construct(self)
        OutroScene.construct(self)