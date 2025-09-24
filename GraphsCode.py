# ==============================================================================
# TÍTULO: MERCADO DE BIENES - Código Interactivo con Widgets
# ==============================================================================

# ------------------------------------------------------------------------------
# SECCIÓN 1: IMPORTACIÓN DE LIBRERÍAS
# ------------------------------------------------------------------------------
import numpy as np                            # Para cálculos numéricos
import matplotlib.pyplot as plt               # Para crear gráficos
import ipywidgets as widgets                  # Para controles interactivos (sliders)
from IPython.display import display           # Para mostrar la interfaz en Jupyter

# ------------------------------------------------------------------------------
# SECCIÓN 2: DEFINICIÓN DE LA FUNCIÓN PRINCIPAL
# ------------------------------------------------------------------------------
def crear_grafica_mercado_bienes(
    g0=200,        # Gasto Público inicial
    t1=0.2,        # Tasa Impositiva inicial
    i0=150,        # Inversión Autónoma inicial
    nx0=100        # Exportaciones Netas Autónomas inicial
):
    """
    Devuelve una interfaz interactiva para el modelo de mercado de bienes (Cruz Keynesiana)
    permitiendo manipular los parámetros y visualizar la gráfica en tiempo real.

    Parámetros iniciales:
        g0: Gasto Público
        t1: Tasa Impositiva
        i0: Inversión Autónoma
        nx0: Exportaciones Netas Autónomas
    """

    # --------------------------------------------------------------------------
    # SUBSECCIÓN 2.1: CREACIÓN DE LOS SLIDERS (widgets.FloatSlider)
    # --------------------------------------------------------------------------
    slider_layout = widgets.Layout(width='80%')  # Establece ancho de los sliders

    # Slider para el Gasto Público
    gasto_slider = widgets.FloatSlider(
        value=g0, min=100, max=300, step=10,
        description="Gasto Público (g₀)", layout=slider_layout, readout_format='.0f'
    )
    # Slider para la Tasa Impositiva
    tasa_slider = widgets.FloatSlider(
        value=t1, min=0.1, max=0.5, step=0.05,
        description="Tasa Impositiva (t₁)", layout=slider_layout, readout_format='.2f'
    )
    # Slider para la Inversión Autónoma
    inversion_slider = widgets.FloatSlider(
        value=i0, min=50, max=250, step=10,
        description="Inversión Autónoma (i₀)", layout=slider_layout, readout_format='.0f'
    )
    # Slider para Exportaciones Netas Autónomas
    nx_slider = widgets.FloatSlider(
        value=nx0, min=-50, max=200, step=10,
        description="Exp. Netas Autónomas (nx₀)", layout=slider_layout, readout_format='.0f'
    )

    # Widget de salida para mostrar la gráfica
    plot_output = widgets.Output()

    # --------------------------------------------------------------------------
    # SUBSECCIÓN 2.2: FUNCIÓN PARA DIBUJAR LA GRÁFICA ECONÓMICA
    # --------------------------------------------------------------------------
    def dibujar_grafica(g0, t1, i0, nx0):
        with plot_output:
            plot_output.clear_output(wait=True)  # Limpia la gráfica anterior

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
            ax.plot(Y_eq, Y_eq, 'o', color='red', markersize=10, label=f'Equilibrio: Y={Y_eq:.1f}')
            ax.vlines(Y_eq, 0, Y_eq, color='red', linestyle=':', alpha=0.7)
            ax.hlines(Y_eq, 0, Y_eq, color='red', linestyle=':', alpha=0.7)

            # --- Estilización y anotaciones ---
            ax.set_title(f"Multiplicador: {alpha:.2f} | Ingreso de Equilibrio: {Y_eq:.1f}", fontsize=14)
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

    # --------------------------------------------------------------------------
    # SUBSECCIÓN 2.6: DIBUJO INICIAL DE LA GRÁFICA
    # --------------------------------------------------------------------------
    actualizar_grafica()  # Muestra la gráfica con los valores iniciales

    # --------------------------------------------------------------------------
    # SUBSECCIÓN 2.7: RETORNO DE LA INTERFAZ COMPLETA
    # --------------------------------------------------------------------------
    return ui

# ------------------------------------------------------------------------------
# SECCIÓN 3: EJECUCIÓN DEL CÓDIGO EN EL CUADERNO
# ------------------------------------------------------------------------------
# Ejemplo de uso: muestra la interfaz interactiva con valores iniciales personalizados
display(crear_grafica_mercado_bienes())



# ==============================================================================
# ==============================================================================
# ==============================================================================


# ==============================================================================
# TÍTULO: MERCADO DE DINERO (MODELO LM) 
# ==============================================================================

# ------------------------------------------------------------------------------
# SECCIÓN 1: DEFINICIÓN DE LA FUNCIÓN PRINCIPAL
# ------------------------------------------------------------------------------
def crear_grafica_mercado_dinero(
    Ms=150,       # Oferta Monetaria inicial
    Y=800,        # Nivel de Ingreso inicial
    P=1           # Nivel de Precios inicial
):
    """
    Devuelve una interfaz interactiva para el modelo de mercado de dinero (Modelo LM)
    permitiendo manipular los parámetros y visualizar la gráfica en tiempo real.

    Parámetros iniciales:
        Ms: Oferta Monetaria
        Y: Nivel de Ingreso
        P: Nivel de Precios
    """

    # --------------------------------------------------------------------------
    # SUBSECCIÓN 1.1: CREACIÓN DE LOS SLIDERS (widgets.FloatSlider)
    # --------------------------------------------------------------------------
    slider_layout = widgets.Layout(width='80%')  # Establece ancho de los sliders

    # Slider para Oferta Monetaria
    oferta_slider = widgets.FloatSlider(
        value=Ms, min=50, max=250, step=10,
        description="Oferta Monetaria (Ms)", layout=slider_layout, readout_format='.0f'
    )
    # Slider para Nivel de Ingreso
    ingreso_slider = widgets.FloatSlider(
        value=Y, min=500, max=1500, step=25,
        description="Nivel de Ingreso (Y)", layout=slider_layout, readout_format='.0f'
    )
    # Slider para Nivel de Precios
    precio_slider = widgets.FloatSlider(
        value=P, min=0.5, max=2, step=0.1,
        description="Nivel de Precios (P)", layout=slider_layout, readout_format='.1f'
    )

    # Widget de salida para mostrar la gráfica
    plot_output = widgets.Output()

    # --------------------------------------------------------------------------
    # SUBSECCIÓN 1.2: FUNCIÓN PARA DIBUJAR LA GRÁFICA ECONÓMICA
    # --------------------------------------------------------------------------
    def dibujar_grafica(Ms, Y, P):
        with plot_output:
            plot_output.clear_output(wait=True)  # Limpia la gráfica anterior

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
            ax.plot(Ms_real, i_eq, 'o', color='black', markersize=10, label=f'Equilibrio: i={i_eq:.2f}')
            ax.hlines(i_eq, 0, Ms_real, color='black', linestyle=':', alpha=0.8)

            # --- Estilización y anotaciones ---
            ax.set_title(f"Tasa de Interés de Equilibrio: {i_eq:.2f}%", fontsize=14)
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
    actualizar_grafica()  # Muestra la gráfica con los valores iniciales

    # --------------------------------------------------------------------------
    # SUBSECCIÓN 1.7: RETORNO DE LA INTERFAZ COMPLETA
    # --------------------------------------------------------------------------
    return ui

# ------------------------------------------------------------------------------
# SECCIÓN 2: EJECUCIÓN DEL CÓDIGO EN EL CUADERNO
# ------------------------------------------------------------------------------
# Ejemplo de uso: muestra la interfaz interactiva con valores iniciales personalizados
display(crear_grafica_mercado_dinero(150, 800, 1))


# ==============================================================================
# ==============================================================================
# ==============================================================================


# ==============================================================================
# TÍTULO: MERCADO DE DIVISAS (PARIDAD DE INTERESES)
# ==============================================================================
"""
Análisis Interactivo del Mercado de Divisas.

Este script visualiza la condición de paridad de intereses no cubierta, que
determina el tipo de cambio de equilibrio. El equilibrio se da cuando el
rendimiento de los depósitos en moneda nacional es igual al rendimiento
esperado de los depósitos en moneda extranjera.
"""
def crear_grafica_mercado_divisas():
    """
    Crea y devuelve una interfaz de usuario interactiva para el modelo
    del mercado de divisas.
    """
    # --- 2.1. Creación de Widgets de la Interfaz ---
    plot_output = widgets.Output()
    slider_layout = widgets.Layout(width='80%')

    # Widgets para controlar los parámetros del modelo.
    r_nac_label = widgets.Label("Tasa de Interés Nacional (R):")
    r_nac_slider = widgets.FloatSlider(value=5, min=1, max=10, step=0.5, layout=slider_layout, readout_format='.1f')
    
    r_ext_label = widgets.Label("Tasa de Interés Extranjera (R*):")
    r_ext_slider = widgets.FloatSlider(value=5, min=1, max=10, step=0.5, layout=slider_layout, readout_format='.1f')

    ee_label = widgets.Label("Tipo de Cambio Esperado (Eᵉ):")
    ee_slider = widgets.FloatSlider(value=1.0, min=0.5, max=2.0, step=0.05, layout=slider_layout, readout_format='.2f')

    # --- 2.2. Función de Dibujo de la Gráfica ---
    def dibujar_grafica(R, R_star, Ee):
        with plot_output:
            plot_output.clear_output(wait=True)

            # --- Subsección 2.2.1: Cálculos del Modelo Económico ---
            # Se calcula el tipo de cambio de equilibrio (E) despejando de la paridad de intereses:
            # R = R* + (Ee - E) / E  =>  E = Ee / (1 + R - R*)
            # Se añade un control para evitar divisiones por cero o valores negativos si R - R* <= -1
            if (1 + (R/100) - (R_star/100)) <= 0:
                E_eq = float('nan') # Resultado indefinido
            else:
                E_eq = Ee / (1 + (R/100) - (R_star/100))

            # --- Subsección 2.2.2: Creación de la Gráfica con Matplotlib ---
            fig, ax = plt.subplots(figsize=(10, 8))
            
            # Rango para el eje Y (Tipo de Cambio Spot)
            E_range = np.linspace(0.5, 2.5, 100)
            
            # Calcular el rendimiento esperado de los depósitos en moneda extranjera.
            retorno_esperado_ext = (R_star/100) + (Ee - E_range) / E_range
            
            # Dibujar las curvas de rendimiento.
            ax.plot(retorno_esperado_ext * 100, E_range, color='darkorange', linewidth=3, label='Rendimiento Esperado Depósitos Extranjeros')
            ax.axvline(x=R, color='indigo', linewidth=3, label='Rendimiento Depósitos Nacionales (R)')
            
            # Marcar el punto de equilibrio.
            if not np.isnan(E_eq):
                ax.plot(R, E_eq, 'o', color='black', markersize=12, label=f'Equilibrio (E={E_eq:.3f})')
                ax.hlines(E_eq, -100, R, color='black', linestyle=':', alpha=0.8)

            # --- Subsección 2.2.3: Estilo y Formato ---
            ax.set_title("Equilibrio en el Mercado de Divisas", fontsize=16)
            ax.set_xlabel("Tasa de Rendimiento (%)", fontsize=12)
            ax.set_ylabel("Tipo de Cambio Spot (E)", fontsize=12)
            ax.grid(True, linestyle=':', alpha=0.6)
            ax.legend(loc="upper right")
            
            ax.set_xlim(left=-10, right=20)
            ax.set_ylim(bottom=0.5, top=2.5)

            plt.tight_layout()
            plt.show()

    # --- 2.3. Lógica de Interacción (Observadores) ---
    def on_value_change(change):
        dibujar_grafica(r_nac_slider.value, r_ext_slider.value, ee_slider.value)

    for slider in [r_nac_slider, r_ext_slider, ee_slider]:
        slider.observe(on_value_change, names='value')

    # --- 2.4. Organización de la Interfaz de Usuario (UI) ---
    controles = widgets.VBox([
        widgets.VBox([r_nac_label, r_nac_slider]),
        widgets.VBox([r_ext_label, r_ext_slider]),
        widgets.VBox([ee_label, ee_slider])
    ], layout=widgets.Layout(width='400px'))
    
    ui = widgets.HBox([controles, plot_output], layout=widgets.Layout(align_items='center'))
    
    on_value_change(None)
    return ui

# ==============================================================================
# TÍTULO: MODELO DD-AA DE KRUGMAN
# ==============================================================================
"""
Análisis Interactivo del Modelo DD-AA para una Economía Abierta.

Este script visualiza el modelo DD-AA, que determina el equilibrio simultáneo
del producto (Y) y el tipo de cambio (E). La curva DD representa el equilibrio
en el mercado de bienes y la curva AA el equilibrio en el mercado de activos.
"""
def crear_grafica_dd_aa():
    """
    Crea y devuelve una interfaz de usuario interactiva para el modelo DD-AA.
    """
    # --- 2.1. Creación de Widgets de la Interfaz ---
    plot_output = widgets.Output()
    slider_layout = widgets.Layout(width='80%')

    # Widgets para la curva DD (Política Fiscal)
    gasto_slider = widgets.FloatSlider(value=200, min=100, max=300, step=10, layout=slider_layout, readout_format='.0f')
    tasa_imp_slider = widgets.FloatSlider(value=0.2, min=0.1, max=0.5, step=0.05, layout=slider_layout, readout_format='.2f')

    # Widgets para la curva AA (Política Monetaria)
    oferta_slider = widgets.FloatSlider(value=300, min=200, max=400, step=10, layout=slider_layout, readout_format='.0f')
    precio_slider = widgets.FloatSlider(value=1.0, min=0.5, max=2.0, step=0.1, layout=slider_layout, readout_format='.1f')
    
    # Widgets para parámetros externos (afectan a ambas curvas)
    r_ext_slider = widgets.FloatSlider(value=5.0, min=1.0, max=10.0, step=0.5, layout=slider_layout, readout_format='.1f')
    ee_slider = widgets.FloatSlider(value=1.0, min=0.5, max=1.5, step=0.05, layout=slider_layout, readout_format='.2f')


    # --- 2.2. Función de Dibujo de la Gráfica ---
    def dibujar_grafica(G, T, Ms, P, R_star, Ee):
        with plot_output:
            plot_output.clear_output(wait=True)
            
            # --- Subsección 2.2.1: Parámetros Fijos del Modelo ---
            # Parámetros comunes
            c0 = 50; c1 = 0.6; I0 = 150; NX0 = -50
            
            # Parámetros DD
            q = 100 # Sensibilidad de NX a E
            m = 0.1 # Propensión marginal a importar
            
            # Parámetros AA
            k = 0.25 # Sensibilidad de L a Y
            h = 20  # Sensibilidad de L a R

            # --- Subsección 2.2.2: Cálculos del Modelo Económico ---
            Y_range = np.linspace(500, 2500, 200)

            # Ecuación de la Curva DD: E = f(Y)
            # Y = (c0 - c1*T*Y + I0 + G + NX0 + q*E - m*Y) => Despejar E
            # Simplificado con T como T = t*Y
            multiplicador_inv = (1 - c1 * (1 - T) + m)
            gasto_autonomo = c0 + I0 + G + NX0
            E_dd = (Y_range * multiplicador_inv - gasto_autonomo) / q
            
            # Ecuación de la Curva AA: E = f(Y)
            # M/P = k*Y - h*R y R = R* + (Ee - E)/E => Aproximación: R ≈ R* + Ee/E - 1
            # Despejando E: E = Ee / (1 + R - R*) donde R = (k*Y - Ms/P)/h
            R = (k * Y_range - (Ms / P)) / h
            E_aa = Ee / (1 + (R/100) - (R_star/100))
            
            # --- Subsección 2.2.3: Cálculo del Punto de Equilibrio ---
            # Encontrar la intersección numérica de DD y AA
            idx = np.argwhere(np.diff(np.sign(E_dd - E_aa))).flatten()
            if idx.size > 0:
                Y_eq = Y_range[idx[0]]
                E_eq = E_dd[idx[0]]
                eq_label = f'Equilibrio (Y={Y_eq:.1f}, E={E_eq:.2f})'
            else:
                Y_eq, E_eq = (float('nan'), float('nan'))
                eq_label = 'Equilibrio no encontrado'


            # --- Subsección 2.2.4: Creación de la Gráfica con Matplotlib ---
            fig, ax = plt.subplots(figsize=(10, 8))
            
            ax.plot(Y_range, E_dd, color='crimson', linewidth=3, label='Curva DD (Mercado de Bienes)')
            ax.plot(Y_range, E_aa, color='royalblue', linewidth=3, label='Curva AA (Mercado de Activos)')
            
            # Marcar el punto de equilibrio
            if not np.isnan(Y_eq):
                ax.plot(Y_eq, E_eq, 'o', color='black', markersize=12, label=eq_label)
                ax.vlines(Y_eq, 0, E_eq, color='black', linestyle=':', alpha=0.8)
                ax.hlines(E_eq, 0, Y_eq, color='black', linestyle=':', alpha=0.8)

            # --- Subsección 2.2.5: Estilo y Formato ---
            ax.set_title("Equilibrio del Modelo DD-AA", fontsize=16)
            ax.set_xlabel("Producción / Renta (Y)", fontsize=12)
            ax.set_ylabel("Tipo de Cambio (E)", fontsize=12)
            ax.grid(True, linestyle=':', alpha=0.6)
            ax.legend(loc="upper right")
            
            ax.set_xlim(left=500, right=2500)
            ax.set_ylim(bottom=0, top=2.5)

            plt.tight_layout()
            plt.show()

    # --- 2.3. Lógica de Interacción (Observadores) ---
    def on_value_change(change):
        dibujar_grafica(gasto_slider.value, tasa_imp_slider.value, oferta_slider.value, 
                        precio_slider.value, r_ext_slider.value, ee_slider.value)
    
    sliders = [gasto_slider, tasa_imp_slider, oferta_slider, precio_slider, r_ext_slider, ee_slider]
    for slider in sliders:
        slider.observe(on_value_change, names='value')

    # --- 2.4. Organización de la Interfaz de Usuario (UI) ---
    controles_dd = widgets.VBox([
        widgets.HTML("<b>Política Fiscal (desplaza DD)</b>"),
        widgets.VBox([widgets.Label("Gasto Público (G):"), gasto_slider]),
        widgets.VBox([widgets.Label("Tasa Impositiva (T):"), tasa_imp_slider])
    ])
    controles_aa = widgets.VBox([
        widgets.HTML("<br><b>Política Monetaria (desplaza AA)</b>"),
        widgets.VBox([widgets.Label("Oferta Monetaria (Ms):"), oferta_slider]),
        widgets.VBox([widgets.Label("Nivel de Precios (P):"), precio_slider])
    ])
    controles_ext = widgets.VBox([
        widgets.HTML("<br><b>Parámetros Externos</b>"),
        widgets.VBox([widgets.Label("Tasa Interés Extranjera (R*):"), r_ext_slider]),
        widgets.VBox([widgets.Label("Tipo Cambio Esperado (Eᵉ):"), ee_slider])
    ])

    controles = widgets.VBox([controles_dd, controles_aa, controles_ext], layout=widgets.Layout(width='400px'))
    ui = widgets.HBox([controles, plot_output], layout=widgets.Layout(align_items='center'))
    
    on_value_change(None)
    return ui

