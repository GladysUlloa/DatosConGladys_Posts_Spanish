from manim import * #Recomendable cargarlo separado

%%manim -qm -v WARNING MaximaVerosimilitud

class MaximaVerosimilitud(Scene):
    def construct(self):
        self.camera.background_color = "#ffffff"

        # Ejes configurados profesionalmente
        axes = Axes(
            x_range=[-1, 4, 0.5],
            y_range=[0, 1.1, 0.2],
            x_length=10,
            y_length=5,
            axis_config={
                "color": DARK_GRAY,
                "stroke_width": 2,
                "include_numbers": True,
                "font_size": 28,
            },
            tips=False,
        ).to_edge(DOWN).shift(UP * 0.5)

        # Etiquetas de ejes
        x_label = axes.get_x_axis_label(Tex(r"$\theta$", color=BLACK))
        y_label = axes.get_y_axis_label(Tex(r"$L(\theta)$", color=BLACK))

        # Función de verosimilitud (simulada con normal)
        def likelihood(theta):
            return np.exp(-(theta - 1.5)**2 / (2 * 0.4**2))

        curve = axes.plot(
            likelihood,
            color=BLUE_E,
            stroke_width=6
        )

        # Sombrear la región bajo la curva
        shaded_area = axes.get_area(
            curve,
            x_range=[-1, 4],
            color=BLUE_E,
            opacity=0.3
        )

        # Punto máximo (estimación)
        max_x = 1.5
        max_y = likelihood(max_x)
        dot = Dot(point=axes.coords_to_point(max_x, max_y), color=RED, radius=0.08)
        vline = axes.get_vertical_line(axes.coords_to_point(max_x, max_y), color=RED, stroke_width=3)
        label = MathTex(r"\hat{\theta} = 1.5", color=RED, font_size=40).next_to(vline, DOWN)

        # Título
        title = Tex("Estimación por Máxima Verosimilitud", font_size=48, color=BLACK).to_edge(UP)

        # Animaciones lentas y elegantes
        self.play(Write(title), run_time=2)
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=2)
        self.play(Create(curve), run_time=3)
        self.play(FadeIn(shaded_area), run_time=2)
        self.play(FadeIn(dot), GrowFromEdge(vline, DOWN), Write(label), run_time=2)
        self.wait(4)
