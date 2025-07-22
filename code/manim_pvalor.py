from manim import * 

%%manim -qm -v WARNING PValueVisualization

class PValueVisualization(Scene):
    def construct(self):
        # Título
        title = Text("Visualización del p-valor", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Crear ejes, más centrados y arriba, eje X más largo
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 0.5, 0.1],
            x_length=12,  # aumenté de 10 a 12 para curva más larga
            y_length=3,
            axis_config={"include_tip": False},
            tips=False,
            x_axis_config={"numbers_to_include": [-3, -2, -1, 0, 1, 2, 3]},
        ).shift(UP * 0.5)

        x_label = axes.get_x_axis_label("Z")
        y_label = axes.get_y_axis_label("Densidad")

        self.play(Create(axes), Write(x_label), Write(y_label))

        # Función densidad normal estándar
        def normal_dist(x):
            return 1 / (2 * PI) ** 0.5 * np.exp(-0.5 * x ** 2)

        normal_curve = axes.plot(normal_dist, color=BLUE, stroke_width=3)
        self.play(Create(normal_curve))

        # Valor crítico (z = 1.96)
        critical_value = 1.96
        crit_point = Dot(axes.c2p(critical_value, 0), color=RED)
        crit_label = MathTex(r"z=1.96").next_to(crit_point, UR, buff=0.5)

        self.play(FadeIn(crit_point), Write(crit_label))

        # Área de p-valor (cola derecha) en rojo
        p_value_area = axes.get_area(normal_curve, x_range=[critical_value, 4], color=RED, opacity=0.5)
        self.play(FadeIn(p_value_area))

        # Área complementaria (cola izquierda) en azul claro para contraste
        left_area = axes.get_area(normal_curve, x_range=[-4, -critical_value], color=BLUE, opacity=0.3)
        self.play(FadeIn(left_area))

        # Texto explicativo alineado a la izquierda, fuera de la gráfica
        explanation = (
            Text(
                "Área roja = p-valor\n"
                "Probabilidad de obtener un valor\n"
                "igual o más extremo que z=1.96\n"
                "bajo hipótesis nula",
                font_size=24,
                line_spacing=1.2,
                t2c={"p-valor": RED},
            )
            .to_edge(LEFT)
            .shift(UP * 0.2)
        )
        self.play(Write(explanation))

        self.wait(5)
