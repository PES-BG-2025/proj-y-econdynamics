# ==============================================================================
# TÍTULO: MERCADO DE BIENES - Código Interactivo con Widgets
# ==============================================================================

# SECCIÓN 1: IMPORTACIÓN DE LIBRERÍAS
import numpy as np                            # Para cálculos numéricos
import matplotlib.pyplot as plt               # Para crear gráficos
import ipywidgets as widgets                  # Para controles interactivos (sliders)
from IPython.display import display           # Para mostrar la interfaz en Jupyter


# SECCIÓN 2: DEFINICIÓN DE LA FUNCIÓN PRINCIPAL
def crear_grafica_mercado_bienes(
    g0=200,        # Gasto Público inicial
    t1=0.2,        # Tasa Impositiva inicial
    i0=150,        # Inversión Autónoma inicial
    nx0=100        # Exportaciones Netas Autónomas inicial
):
    """
        Parámetros iniciales:
        g0: Gasto Público
        t1: Tasa Impositiva
        i0: Inversión Autónoma
        nx0: Exportaciones Netas Autónomas
    """

    # --------------------------------------------------------------------------
    # SUBSECCIÓN 2.1: CREACIÓN DE LOS SLIDERS
    # --------------------------------------------------------------------------
    slider_layout = widgets.Layout(width='80%') 

    # Slider para el Gasto Público
    gasto_slider = widgets.FloatSlider(
        value=g0, min=100, max=300, step=10,
        description="Gasto Público (g₀)", layout=slider_layout)
    # Slider para la Tasa Impositiva
    tasa_slider = widgets.FloatSlider(
        value=t1, min=0.1, max=0.5, step=0.05,
        description="Tasa Impositiva (t₁)", layout=slider_layout)
    # Slider para la Inversión Autónoma
    inversion_slider = widgets.FloatSlider(
        value=i0, min=50, max=250, step=10,
        description="Inversión Autónoma (i₀)", layout=slider_layout)
    # Slider para Exportaciones Netas Autónomas
    nx_slider = widgets.FloatSlider(
        value=nx0, min=-50, max=200, step=10,
        description="Exp. Netas Autónomas (nx₀)", layout=slider_layout)

    # Widget de salida para mostrar la gráfica
    plot_output = widgets.Output()

    # --------------------------------------------------------------------------
    # SUBSECCIÓN 2.2: FUNCIÓN PARA DIBUJAR LA GRÁFICA ECONÓMICA
    # --------------------------------------------------------------------------
    def dibujar_grafica(g0, t1, i0, nx0):
        with plot_output:
            plot_output.clear_output(wait=True) 

            # Parámetros fijos del modelo
            c0 = 50    # Consumo autónomo
            c1 = 0.6   # Propensión marginal a consumir

            # --- Cálculos económicos ---
            alpha = 1 / (1 - c1 * (1 - t1))          # Multiplicador Keynesiano
            A = c0 + i0 + g0 + nx0                   # Suma de componentes autónomos
            Y_eq = alpha * A                         # Ingreso de equilibrio

            # --- Preparación de datos para la gráfica ---
            Y_MAX_FIJO = 2500                        # Rango fijo para los ejes
            Y_range = np.linspace(0, Y_MAX_FIJO, 100)
            DA = A + c1 * (1 - t1) * Y_range         # Gasto Agregado (DA)

            # --- Creación de la gráfica ---
            fig, ax = plt.subplots(figsize=(9, 6))
            ax.plot(Y_range, Y_range, '--', color='gray', label='Y = DA (Equilibrio)')
            ax.plot(Y_range, DA, '-', color='deepskyblue', linewidth=2.5, label='Gasto Agregado (DA)')
            ax.plot(Y_eq, Y_eq, 'o', color='red', markersize=10, label=f'Equilibrio: Y={Y_eq}')
            ax.vlines(Y_eq, 0, Y_eq, color='red', linestyle=':', alpha=0.7)
            ax.hlines(Y_eq, 0, Y_eq, color='red', linestyle=':', alpha=0.7)

            # --- Estilización y anotaciones ---
            ax.set_title(f"Multiplicador: {alpha} | Ingreso de Equilibrio: {Y_eq}", fontsize=14)
            ax.set_xlabel("Ingreso / Producción (Y)", fontsize=12)
            ax.set_ylabel("Gasto Agregado (DA)", fontsize=12)
            ax.set_xlim(0, Y_MAX_FIJO)
            ax.set_ylim(0, Y_MAX_FIJO)
            ax.grid(True, linestyle=':', alpha=0.5)
            ax.legend(loc='upper left')
            plt.tight_layout()
            plt.show()

    # --------------------------------------------------------------------------
    # SUBSECCIÓN 2.3: FUNCIÓN DE ACTUALIZACIÓN DE LA GRÁFICA
    # --------------------------------------------------------------------------
    def actualizar_grafica(change=None):
        """
        Toma los valores actuales de los sliders y actualiza la gráfica.
        Se ejecuta al mover cualquier slider.
        """
        dibujar_grafica(
            gasto_slider.value,
            tasa_slider.value,
            inversion_slider.value,
            nx_slider.value
        )

    # --------------------------------------------------------------------------
    # SUBSECCIÓN 2.4: CONEXIÓN DE SLIDERS Y FUNCIÓN DE DIBUJO
    # --------------------------------------------------------------------------
    # Se conecta cada slider para que, al cambiar, se actualice la gráfica automáticamente
    for slider in [gasto_slider, tasa_slider, inversion_slider, nx_slider]:
        slider.observe(actualizar_grafica, names='value')

    # --------------------------------------------------------------------------
    # SUBSECCIÓN 2.5: ORGANIZACIÓN DE LA INTERFAZ GRÁFICA
    # --------------------------------------------------------------------------
    # Se agrupan los sliders (controles) en una caja vertical
    controles = widgets.VBox(
        [gasto_slider, tasa_slider, inversion_slider, nx_slider],
        layout=widgets.Layout(width='350px')
    )
    # Se agrupan los controles y la gráfica en una caja horizontal
    ui = widgets.HBox([controles, plot_output], layout=widgets.Layout(align_items='center'))


    actualizar_grafica() 
    return ui

display(crear_grafica_mercado_bienes())



# ==============================================================================
# ==============================================================================
# ==============================================================================


# ==============================================================================
# TÍTULO: MERCADO DE DINERO (MODELO LM) 
# ==============================================================================

# SECCIÓN 1: DEFINICIÓN DE LA FUNCIÓN PRINCIPAL

def crear_grafica_mercado_dinero(
    Ms=150,       # Oferta Monetaria inicial
    Y=800,        # Nivel de Ingreso inicial
    P=1           # Nivel de Precios inicial
):
    """
    Parámetros iniciales:
        Ms: Oferta Monetaria
        Y: Nivel de Ingreso
        P: Nivel de Precios
    """

    # --------------------------------------------------------------------------
    # SUBSECCIÓN 1.1: CREACIÓN DE LOS SLIDERS
    # --------------------------------------------------------------------------
    slider_layout = widgets.Layout(width='80%')  

    # Slider para Oferta Monetaria
    oferta_slider = widgets.FloatSlider(
        value=Ms, min=50, max=250, step=10,
        description="Oferta Monetaria (Ms)", layout=slider_layout)
    # Slider para Nivel de Ingreso
    ingreso_slider = widgets.FloatSlider(
        value=Y, min=500, max=1500, step=25,
        description="Nivel de Ingreso (Y)", layout=slider_layout)
    # Slider para Nivel de Precios
    precio_slider = widgets.FloatSlider(
        value=P, min=1, max=2, step=0.1,
        description="Nivel de Precios (P)", layout=slider_layout)

    # Widget de salida para mostrar la gráfica
    plot_output = widgets.Output()

    # --------------------------------------------------------------------------
    # SUBSECCIÓN 1.2: FUNCIÓN PARA DIBUJAR LA GRÁFICA ECONÓMICA
    # --------------------------------------------------------------------------
    def dibujar_grafica(Ms, Y, P):
        with plot_output:
            plot_output.clear_output(wait=True)

            # Parámetros fijos del modelo de demanda de dinero: L = kY - hi
            k = 0.5   # Sensibilidad de la demanda de dinero al ingreso
            h = 10    # Sensibilidad de la demanda de dinero a la tasa de interés

            # --- Cálculos económicos ---
            Ms_real = Ms / P                             # Oferta real de dinero
            i_eq = (k * Y - Ms_real) / h                 # Tasa de interés de equilibrio

            # --- Preparación de datos para la gráfica ---
            I_MAX_FIJO = 50                              # Rango fijo para tasa de interés
            M_MAX_FIJO = 500                             # Rango fijo para cantidad de dinero real
            i_range = np.linspace(0, I_MAX_FIJO, 100)    # Eje de tasas de interés
            Md = k * Y - h * i_range                     # Demanda de dinero (Md)

            # --- Creación de la gráfica ---
            fig, ax = plt.subplots(figsize=(9, 6))
            ax.plot(Md, i_range, '-', color='orange', linewidth=2.5, label='Demanda de Dinero (Md)')
            ax.axvline(x=Ms_real, color='skyblue', linewidth=3, linestyle='-', label='Oferta Real (Ms/P)')
            ax.plot(Ms_real, i_eq, 'o', color='black', markersize=10, label=f'Equilibrio: i={i_eq}')
            ax.hlines(i_eq, 0, Ms_real, color='black', linestyle=':', alpha=0.8)

            # --- Estilización y anotaciones ---
            ax.set_title(f"Tasa de Interés de Equilibrio: {i_eq}%", fontsize=14)
            ax.set_xlabel("Cantidad Real de Dinero (M/P)", fontsize=12)
            ax.set_ylabel("Tasa de Interés (i)", fontsize=12)
            ax.set_xlim(0, M_MAX_FIJO)
            ax.set_ylim(0, I_MAX_FIJO)
            ax.grid(True, linestyle=':', alpha=0.5)
            ax.legend(loc='upper right')
            plt.tight_layout()
            plt.show()

    # --------------------------------------------------------------------------
    # SUBSECCIÓN 1.3: FUNCIÓN DE ACTUALIZACIÓN DE LA GRÁFICA
    # --------------------------------------------------------------------------
    def actualizar_grafica(change=None):
        """
        Toma los valores actuales de los sliders y actualiza la gráfica.
        Se ejecuta al mover cualquier slider.
        """
        dibujar_grafica(
            oferta_slider.value,
            ingreso_slider.value,
            precio_slider.value
        )

    # --------------------------------------------------------------------------
    # SUBSECCIÓN 1.4: CONEXIÓN DE SLIDERS Y FUNCIÓN DE DIBUJO
    # --------------------------------------------------------------------------
    # Se conecta cada slider para que, al cambiar, se actualice la gráfica automáticamente
    for slider in [oferta_slider, ingreso_slider, precio_slider]:
        slider.observe(actualizar_grafica, names='value')

    # --------------------------------------------------------------------------
    # SUBSECCIÓN 1.5: ORGANIZACIÓN DE LA INTERFAZ GRÁFICA
    # --------------------------------------------------------------------------
    # Se agrupan los sliders (controles) en una caja vertical
    controles = widgets.VBox(
        [oferta_slider, ingreso_slider, precio_slider],
        layout=widgets.Layout(width='350px')
    )
    # Se agrupan los controles y la gráfica en una caja horizontal
    ui = widgets.HBox([controles, plot_output], layout=widgets.Layout(align_items='center'))

    # --------------------------------------------------------------------------
    # SUBSECCIÓN 1.6: DIBUJO INICIAL DE LA GRÁFICA
    # --------------------------------------------------------------------------
    actualizar_grafica()  
    return ui

display(crear_grafica_mercado_dinero(150, 800, 1))

# ==============================================================================
# ==============================================================================
# ==============================================================================

# ==============================================================================
# TÍTULO: MERCADO DE DIVISAS (PARIDAD DE INTERESES) 
# ==============================================================================
"""
Objetivo
- La curva de rendimiento esperado de depósitos extranjeros se modela como una recta:
  R_ext(E) = R* + m · (Eᵉ − E), expresada en porcentaje en el eje X.

Cómo usar
- En un notebook de Jupyter:
    display(crear_grafica_mercado_divisas(5, 6, 1))  # R=5, R*=6, Eᵉ=1
"""

# SECCIÓN 1: FUNCIÓN PRINCIPAL PARA CREAR LA INTERFAZ

def crear_grafica_mercado_divisas(
    R: float = 5.0,        # Tasa de Interés Nacional inicial (%)
    R_star: float = 5.0,   # Tasa de Interés Extranjera inicial (%)
    Ee: float = 1.0,       # Tipo de Cambio Esperado inicial
    m: float = 2.0         # Pendiente de la recta (opcional). +m => recta decreciente en E
):
    """
    Devuelve una interfaz interactiva del mercado de divisas con:
    - Curva (recta) del rendimiento esperado: R_ext(E) = R* + m (Eᵉ − E)  [en %].
    - Eje Y (E) fijo en [0, 10] y eje X (rendimiento) fijo en [0, 10].

    Parámetros:
        R (float): Tasa de interés nacional inicial (%).
        R_star (float): Tasa de interés extranjera inicial (%).
        Ee (float): Tipo de cambio esperado inicial.
        m (float): Pendiente de la recta (porcentaje por unidad de E). No es slider, pero sí parámetro.
    """
    # --------------------------------------------------------------------------
    # 1.1) Widgets (sliders y etiquetas)
    # --------------------------------------------------------------------------
    plot_output = widgets.Output()
    slider_layout = widgets.Layout(width='80%')

    # Sliders con sus etiquetas
    r_nac_label = widgets.Label("Tasa de Interés Nacional (R):")
    r_nac_slider = widgets.FloatSlider(
        value=R, min=1, max=8, step=0.5, layout=slider_layout)

    r_ext_label = widgets.Label("Tasa de Interés Extranjera (R*):")
    r_ext_slider = widgets.FloatSlider(
        value=R_star, min=1, max=8, step=0.5, layout=slider_layout)
    r_ext_slider.readout_format = '.1f'

    ee_label = widgets.Label("Tipo de Cambio Esperado (Eᵉ):")
    ee_slider = widgets.FloatSlider(
        value=Ee, min=0.5, max=2.5, step=0.05, layout=slider_layout)

    # --------------------------------------------------------------------------
    # 1.2) Función interna de dibujo de la gráfica
    # --------------------------------------------------------------------------
    def dibujar_grafica(R_val, R_star_val, Ee_val):
        with plot_output:
            plot_output.clear_output(wait=True)

            # --- 1.2.1: Preparación de datos (eje Y) ---
            E_range = np.linspace(0.0, 10.0, 100)  # Tipo de cambio spot (Y)

            # --- 1.2.2: Curva lineal del rendimiento esperado (eje X, en %) ---
            # R_ext(E) = R* + m · (Ee − E)
            r_ext_line = R_star_val + m * (Ee_val - E_range)

            # --- 1.2.3: Equilibrio coherente con la recta ---
            # R = R* + m (Ee − E_eq)  =>  E_eq = Ee − (R − R*) / m
            if m != 0:
                E_eq = Ee_val - (R_val - R_star_val) / m
            else:
                E_eq = float('nan')

            # ------------------------------------------------------------------
            # 1.2.4: Creación de la gráfica
            # ------------------------------------------------------------------
            fig, ax = plt.subplots(figsize=(10, 7))

            visible = (r_ext_line >= 0) & (r_ext_line <= 10)
            if np.any(visible):
                ax.plot(r_ext_line[visible], E_range[visible],
                        color='darkorange', linewidth=3,
                        label='Rend. Esperado Depósitos Extranjeros (recta)')
            else:
                # Si no hay puntos dentro del marco X, trazar la recta completa (útil para diagnóstico).
                ax.plot(r_ext_line, E_range, color='darkorange', linewidth=3,
                        label='Rend. Esperado Depósitos Extranjeros (recta)')

            # Línea vertical punteada para la tasa nacional R
            ax.axvline(x=R_val, color='indigo', linewidth=2.5, linestyle='--',
                       label='Tasa de Interés Nacional (R)')

            # Punto de equilibrio si cae dentro del marco
            if not np.isnan(E_eq) and 0 <= E_eq <= 10 and 0 <= R_val <= 10:
                ax.plot(R_val, E_eq, 'o', color='black', markersize=10,
                        label=f'Equilibrio (E={E_eq})')
                ax.hlines(E_eq, 0, R_val, color='black', linestyle=':', alpha=0.75)

            # --- 2.2.5: Estilo y límites fijos ---
            ax.set_title("Equilibrio en el Mercado de Divisas (Recta)", fontsize=16)
            ax.set_xlabel("Tasa de Rendimiento (%)", fontsize=12)
            ax.set_ylabel("Tipo de Cambio Spot (E)", fontsize=12)
            ax.set_xlim(0, 10)   # X: 0 a 10 (rendimientos)
            ax.set_ylim(0, 10)   # Y: 0 a 10 (tipo de cambio)
            ax.grid(True, linestyle=':', alpha=0.6)
            ax.legend(loc="upper right")
            plt.tight_layout()
            plt.show()

    # --------------------------------------------------------------------------
    # 1.3) Observadores (reactividad de sliders)
    # --------------------------------------------------------------------------
    def on_value_change(change):
        dibujar_grafica(r_nac_slider.value, r_ext_slider.value, ee_slider.value)

    for slider in (r_nac_slider, r_ext_slider, ee_slider):
        slider.observe(on_value_change, names='value')

    # --------------------------------------------------------------------------
    # 1.4) Layout de la interfaz (UI)
    # --------------------------------------------------------------------------
    controles = widgets.VBox(
        [r_nac_label, r_nac_slider, r_ext_label, r_ext_slider, ee_label, ee_slider],
        layout=widgets.Layout(width='380px')
    )
    ui = widgets.HBox([controles, plot_output], layout=widgets.Layout(align_items='center'))

    # --------------------------------------------------------------------------
    # 1.5) Dibujo inicial con los valores actuales de los sliders
    # --------------------------------------------------------------------------
    dibujar_grafica(r_nac_slider.value, r_ext_slider.value, ee_slider.value)

    # --------------------------------------------------------------------------
    # 1.6) Retornar la interfaz para poder usar: display(crear_grafica_mercado_divisas(...))
    # --------------------------------------------------------------------------
    return ui


# ==============================================================================
# ==============================================================================
# ==============================================================================


# ==============================================================================
# TÍTULO: Dashboard Interactivo del Modelo IS-LM
# ==============================================================================
"""
Modelo IS-LM interactivo.
"""

# ==============================================================================
# 1. FUNCIÓN DE GRÁFICA DEL MODELO IS-LM
# ==============================================================================
def graficar_is_lm(
    c0, c1, T, I0, b,    # Parámetros IS
    k, h, P, M0, G0,     # Parámetros LM
    shock_monetario, shock_fiscal # Shocks de política
):
    """
    Grafica el equilibrio IS-LM inicial y el nuevo equilibrio tras shocks fiscal y monetario,
    permitiendo ajustar los parámetros del modelo.
    """
    # --------------------------------------------------------------------------
    # 1.1. Cálculo del Equilibrio Inicial
    # --------------------------------------------------------------------------
    A_base = c0 - c1 * T + I0 + G0
    Y_eq_base = (h * A_base + b * (M0 / P)) / (h * (1 - c1) + b * k)
    i_eq_base = (A_base / b) - ((1 - c1) / b) * Y_eq_base

    # --------------------------------------------------------------------------
    # 1.2. Cálculo del Equilibrio Tras Shocks
    # --------------------------------------------------------------------------
    M1 = M0 + shock_monetario
    G1 = G0 + shock_fiscal
    A_final = c0 - c1 * T + I0 + G1
    Y_eq_final = (h * A_final + b * (M1 / P)) / (h * (1 - c1) + b * k)
    i_eq_final = (A_final / b) - ((1 - c1) / b) * Y_eq_final

    # --------------------------------------------------------------------------
    # 1.3. Cálculo de las Curvas IS y LM (antes y después del shock)
    # --------------------------------------------------------------------------
    Y_min = max(0, min(Y_eq_base, Y_eq_final) * 0.4)
    Y_max = max(Y_eq_base, Y_eq_final) * 1.6
    Y_range = np.linspace(Y_min, Y_max, 100)

    i_is_base   = (A_base / b) - ((1 - c1) / b) * Y_range
    i_lm_base   = (k / h) * Y_range - (1 / h) * (M0 / P)
    i_is_final  = (A_final / b) - ((1 - c1) / b) * Y_range
    i_lm_final  = (k / h) * Y_range - (1 / h) * (M1 / P)

    # --------------------------------------------------------------------------
    # 1.4. Gráfica de las Curvas IS-LM
    # --------------------------------------------------------------------------
    plt.figure(figsize=(8, 6))
    plt.title('Modelo IS-LM: Shocks Fiscal y Monetario', fontsize=16, weight='bold')

    # Curvas iniciales y equilibrio
    plt.plot(Y_range, i_is_base, color='darkorange', linewidth=2, label='IS (Inicial)')
    plt.plot(Y_range, i_lm_base, color='darkviolet', linewidth=2, label='LM (Inicial)')
    plt.plot(Y_eq_base, i_eq_base, 'ko', markersize=8, label=f'E₀ ({Y_eq_base:.1f}, {i_eq_base:.2f})')

    # Curvas tras shocks y nuevo equilibrio
    if shock_fiscal != 0:
        plt.plot(Y_range, i_is_final, color='sandybrown', linestyle='--', linewidth=2, label="IS (Shock)")
    if shock_monetario != 0:
        plt.plot(Y_range, i_lm_final, color='mediumorchid', linestyle='--', linewidth=2, label="LM (Shock)")
    if shock_monetario != 0 or shock_fiscal != 0:
        plt.plot(Y_eq_final, i_eq_final, 'ko', markersize=8, mfc='white', label=f'E₁ ({Y_eq_final:.1f}, {i_eq_final:.2f})')

    # Etiquetas y formato
    plt.xlabel('Ingreso / Producción (Y)')
    plt.ylabel('Tasa de Interés (i)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.xlim(left=0)
    max_i = max(np.nanmax(i_is_base), np.nanmax(i_lm_base), np.nanmax(i_is_final), np.nanmax(i_lm_final)) * 1.1
    plt.ylim(bottom=0, top=max_i)
    plt.tight_layout()
    plt.show()

# ==============================================================================
# 2. SLIDERS Y DASHBOARD
# ==============================================================================
def dashboard_is_lm():
    """
    Muestra el dashboard interactivo con sliders en una sola columna.
    """
    # --------------------------------------------------------------------------
    # 2.1. Slicers para parámetros IS
    # --------------------------------------------------------------------------
    is_widgets = {
        'c0': widgets.FloatSlider(value=120, min=0, max=300, step=1, description='Consumo autónomo (c0):', style={'description_width': 'initial'}),
        'c1': widgets.FloatSlider(value=0.7, min=0.1, max=0.99, step=0.01, description='PMG Consumir (c1):', style={'description_width': 'initial'}),
        'T': widgets.FloatSlider(value=100, min=0, max=300, step=1, description='Impuestos (T):', style={'description_width': 'initial'}),
        'I0': widgets.FloatSlider(value=180, min=0, max=300, step=1, description='Inversión autónoma (I0):', style={'description_width': 'initial'}),
        'b': widgets.FloatSlider(value=10, min=1, max=50, step=0.1, description='S. de Inversión a i (b):', style={'description_width': 'initial'})
    }
    # --------------------------------------------------------------------------
    # 2.2. Slicers para parámetros LM
    # --------------------------------------------------------------------------
    lm_widgets = {
        'k': widgets.FloatSlider(value=0.6, min=0.01, max=2, step=0.01, description='S. de Ld a Y (k):', style={'description_width': 'initial'}),
        'h': widgets.FloatSlider(value=12, min=1, max=50, step=0.1, description='S. de Ld a i (h):', style={'description_width': 'initial'}),
        'P': widgets.FloatSlider(value=1, min=0.1, max=10, step=0.01, description='Nivel de precios (P):', style={'description_width': 'initial'}),
        'M0': widgets.FloatSlider(value=150, min=0, max=500, step=1, description='Oferta monetaria (M0):', style={'description_width': 'initial'}),
        'G0': widgets.FloatSlider(value=150, min=0, max=500, step=1, description='Gasto público (G0):', style={'description_width': 'initial'})
    }
    # --------------------------------------------------------------------------
    # 2.3. Sliders para shocks de política
    # --------------------------------------------------------------------------
    shock_monetario_slider = widgets.FloatSlider(
        value=0, min=-100, max=100, step=10,
        description='Shock Monetario (ΔM):', style={'description_width': 'initial'}, layout={'width': '300px'}, readout_format='.0f'
    )
    shock_fiscal_slider = widgets.FloatSlider(
        value=0, min=-100, max=100, step=10,
        description='Shock Fiscal (ΔG):', style={'description_width': 'initial'}, layout={'width': '300px'}, readout_format='.0f'
    )

    # --------------------------------------------------------------------------
    # 2.4. Agrupar todos los sliders en una sola columna (VBox)
    # --------------------------------------------------------------------------
    all_sliders = widgets.VBox([
        widgets.HTML('<b>Modelo IS Slicers:</b>'),
        *is_widgets.values(),
        widgets.HTML('<b>Modelo LM Slicers:</b>'),
        *lm_widgets.values(),
        widgets.HTML('<b>Shocks de Política:</b>'),
        shock_monetario_slider,
        shock_fiscal_slider
    ])

    # --------------------------------------------------------------------------
    # 2.5. Conexión de los sliders con la función de gráfica
    # --------------------------------------------------------------------------
    interactive_plot = widgets.interactive_output(
        graficar_is_lm,
        {
            'c0': is_widgets['c0'],
            'c1': is_widgets['c1'],
            'T': is_widgets['T'],
            'I0': is_widgets['I0'],
            'b': is_widgets['b'],
            'k': lm_widgets['k'],
            'h': lm_widgets['h'],
            'P': lm_widgets['P'],
            'M0': lm_widgets['M0'],
            'G0': lm_widgets['G0'],
            'shock_monetario': shock_monetario_slider,
            'shock_fiscal': shock_fiscal_slider
        }
    )

    # --------------------------------------------------------------------------
    # 2.6. Mostrar el dashboard (HBox: sliders + gráfico)
    # --------------------------------------------------------------------------
    ui = widgets.HBox([all_sliders, interactive_plot])
    display(ui)