# ==============================================================================
# TÍTULO: MERCADO DE BIENES (CRUZ KEYNESIANA)
# ==============================================================================
"""
Análisis Interactivo del Mercado de Bienes (Economía Abierta - Modelo IS)

Este script visualiza el modelo de la Cruz Keynesiana para una economía abierta.
Permite al usuario manipular componentes clave del Gasto Agregado para
observar su impacto en el Ingreso de Equilibrio de forma interactiva.
"""

# ------------------------------------------------------------------------------
# SECCIÓN 1: IMPORTACIÓN DE LIBRERÍAS
# ------------------------------------------------------------------------------
# Se importan las librerías necesarias para los cálculos numéricos (numpy),
# la creación de gráficos (matplotlib) y los componentes interactivos (ipywidgets).
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# ------------------------------------------------------------------------------
# SECCIÓN 2: FUNCIÓN PRINCIPAL PARA CREAR LA INTERFAZ
# ------------------------------------------------------------------------------
# Se encapsula toda la lógica en una función principal para mantener el código
# organizado y reutilizable.
def crear_grafica_mercado_bienes():
    """
    Crea y devuelve una interfaz de usuario interactiva para el modelo
    del mercado de bienes y servicios en una economía abierta.
    """
    # --- 2.1. Creación de Widgets de la Interfaz ---
    # Aquí se definen todos los elementos interactivos que el usuario verá.

    # 'plot_output' es el lienzo donde se dibujará nuestra gráfica.
    plot_output = widgets.Output()

    # Layout para estandarizar el ancho de los sliders.
    slider_layout = widgets.Layout(width='80%')

    # Creación de etiquetas y sliders para cada parámetro del modelo.
    # Cada slider controla una variable económica.
    gasto_label = widgets.Label("Gasto Público (g0):")
    gasto_slider = widgets.FloatSlider(value=200, min=100, max=300, step=10, layout=slider_layout, readout_format='.0f')

    tasa_label = widgets.Label("Tasa Impositiva (t1):")
    tasa_slider = widgets.FloatSlider(value=0.2, min=0.1, max=0.5, step=0.05, layout=slider_layout, readout_format='.2f')

    inversion_label = widgets.Label("Inversión Autónoma (i0):")
    inversion_slider = widgets.FloatSlider(value=150, min=50, max=250, step=10, layout=slider_layout, readout_format='.0f')

    nx_label = widgets.Label("Export. Netas Autónomas (nx0):")
    nx_slider = widgets.FloatSlider(value=100, min=-50, max=200, step=10, layout=slider_layout, readout_format='.0f')

    # --- 2.2. Función de Dibujo de la Gráfica ---
    # Esta función contiene la lógica económica y de visualización.
    # Se ejecuta cada vez que un slider cambia de valor.
    def dibujar_grafica(g0, t1, i0, nx0):
        # El bloque 'with' asegura que la gráfica se dibuje en el widget 'plot_output'.
        with plot_output:
            # Limpia la gráfica anterior para evitar superposiciones al actualizar.
            plot_output.clear_output(wait=True)

            # Parámetros fijos del modelo.
            c0 = 50   # Consumo autónomo (asumido)
            c1 = 0.6  # Propensión Marginal a Consumir

            # --- Subsección 2.2.1: Cálculos del Modelo Económico ---
            # 'alpha' es el multiplicador keynesiano.
            alpha = 1 / (1 - c1 * (1 - t1))
            # 'A' es la suma de todos los componentes autónomos del gasto.
            A = c0 + i0 + g0 + nx0
            # 'Y_eq' es el ingreso de equilibrio, donde la producción iguala al gasto.
            Y_eq = alpha * A

            # --- Subsección 2.2.2: Creación de la Gráfica con Matplotlib ---
            fig, ax = plt.subplots(figsize=(10, 7))
            
            # MODIFICACIÓN: Se define un rango FIJO para los ejes.
            Y_MAX_FIJO = 2500
            Y_range = np.linspace(0, Y_MAX_FIJO, 100)
            
            # 'DA' es la función de Gasto Agregado (Demanda Agregada).
            DA = A + c1 * (1 - t1) * Y_range
            
            # Dibujar la línea de 45 grados (condición de equilibrio Y = DA).
            ax.plot(Y_range, Y_range, color='black', linestyle='--', alpha=0.7, label='Y = DA (Condición de Equilibrio)')
            # Dibujar la curva de Gasto Agregado.
            ax.plot(Y_range, DA, color='deepskyblue', linewidth=3, label='Gasto Agregado (DA)')
            # Marcar el punto de equilibrio en la gráfica.
            ax.plot(Y_eq, Y_eq, 'o', color='red', markersize=10, label=f'Punto de Equilibrio (Y={Y_eq:.1f})')
            # Añadir líneas de guía punteadas desde el equilibrio hacia los ejes.
            ax.vlines(Y_eq, 0, Y_eq, color='red', linestyle=':', alpha=0.8)
            ax.hlines(Y_eq, 0, Y_eq, color='red', linestyle=':', alpha=0.8)

            # --- Subsección 2.2.3: Estilo y Formato de la Gráfica ---
            ax.set_title(f"Multiplicador: {alpha:.2f} | Ingreso de Equilibrio: {Y_eq:.1f}", fontsize=16)
            ax.set_xlabel("Ingreso / Producción (Y)", fontsize=12)
            ax.set_ylabel("Gasto Agregado (DA)", fontsize=12)
            ax.grid(True, linestyle=':', alpha=0.6)
            ax.legend(loc="upper left")
            
            # MODIFICACIÓN: Se establecen límites fijos para los ejes X e Y.
            ax.set_xlim(left=0, right=Y_MAX_FIJO)
            ax.set_ylim(bottom=0, top=Y_MAX_FIJO)

            plt.tight_layout() # Ajusta el layout para que no se corten las etiquetas.
            plt.show()         # Muestra la gráfica en el output.

    # --- 2.3. Lógica de Interacción (Observadores) ---
    # Esta sección conecta los sliders con la función de dibujo.
    def on_value_change(change):
        # Llama a la función de dibujo con los valores actuales de todos los sliders.
        dibujar_grafica(gasto_slider.value, tasa_slider.value, inversion_slider.value, nx_slider.value)

    # Se "observa" cada slider; si su 'value' cambia, se llama a la función 'on_value_change'.
    for slider in [gasto_slider, tasa_slider, inversion_slider, nx_slider]:
        slider.observe(on_value_change, names='value')
    
    # --- 2.4. Organización y Visualización de la Interfaz de Usuario (UI) ---
    # Se agrupan los widgets de forma ordenada para presentarlos al usuario.
    
    # Se crea una caja vertical para los controles.
    controles = widgets.VBox([
        widgets.VBox([gasto_label, gasto_slider]),
        widgets.VBox([tasa_label, tasa_slider]),
        widgets.VBox([inversion_label, inversion_slider]),
        widgets.VBox([nx_label, nx_slider])
    ], layout=widgets.Layout(width='400px'))
    
    # Se combinan los controles (izquierda) y la gráfica (derecha) en una caja horizontal.
    ui = widgets.HBox([controles, plot_output], layout=widgets.Layout(align_items='center'))
    
    # --- 2.5. Llamada Inicial para Dibujar la Gráfica ---
    # Se llama a la función una vez al principio para que la gráfica aparezca
    # con los valores iniciales de los sliders.
    on_value_change(None)
    
    # Finalmente, la función devuelve la interfaz completa.
    return ui

# ------------------------------------------------------------------------------
# SECCIÓN 3: EJECUCIÓN Y VISUALIZACIÓN
# ------------------------------------------------------------------------------
# Para mostrar la interfaz interactiva en el cuaderno de Jupyter,
# simplemente llamamos a la función principal.
display(crear_grafica_mercado_bienes())

# ==============================================================================
# ==============================================================================
# ==============================================================================


# ==============================================================================
# TÍTULO: MERCADO DE DINERO
# ==============================================================================
"""
Análisis Interactivo del Mercado de Dinero (Modelo LM)

Este script visualiza el modelo de equilibrio en el mercado monetario.
Permite al usuario manipular la oferta monetaria, el nivel de ingreso y
el nivel de precios para observar su impacto en la tasa de interés de equilibrio.
"""
# ------------------------------------------------------------------------------
# SECCIÓN 2: FUNCIÓN PRINCIPAL PARA CREAR LA INTERFAZ
# ------------------------------------------------------------------------------
# Se encapsula toda la lógica en una función principal para mantener el código
# organizado y reutilizable.
def crear_grafica_mercado_dinero():
    """
    Crea y devuelve una interfaz de usuario interactiva para el modelo
    del mercado de dinero.
    """
    # --- 2.1. Creación de Widgets de la Interfaz ---
    # Aquí se definen todos los elementos interactivos que el usuario verá.

    # 'plot_output' es el lienzo donde se dibujará nuestra gráfica.
    plot_output = widgets.Output()

    # Layout para estandarizar el ancho de los sliders.
    slider_layout = widgets.Layout(width='80%')

    # Creación de etiquetas y sliders para cada parámetro del modelo.
    oferta_label = widgets.Label("Oferta Monetaria (Ms):")
    oferta_slider = widgets.FloatSlider(value=150, min=50, max=250, step=10, layout=slider_layout, readout_format='.0f')

    ingreso_label = widgets.Label("Nivel de Ingreso (Y):")
    ingreso_slider = widgets.FloatSlider(value=800, min=500, max=1500, step=25, layout=slider_layout, readout_format='.0f')
    
    precio_label = widgets.Label("Nivel de Precios (P):")
    precio_slider = widgets.FloatSlider(value=1, min=0.5, max=2, step=0.1, layout=slider_layout, readout_format='.1f')

    # --- 2.2. Función de Dibujo de la Gráfica ---
    # Esta función contiene la lógica económica y de visualización.
    # Se ejecuta cada vez que un slider cambia de valor.
    def dibujar_grafica(Ms, Y, P):
        # El bloque 'with' asegura que la gráfica se dibuje en el widget 'plot_output'.
        with plot_output:
            # Limpia la gráfica anterior para evitar superposiciones al actualizar.
            plot_output.clear_output(wait=True)

            # Parámetros fijos del modelo de demanda de dinero: L = kY - hi
            k = 0.5   # Sensibilidad de la demanda de dinero al ingreso
            h = 10    # Sensibilidad de la demanda de dinero a la tasa de interés

            # --- Subsección 2.2.1: Cálculos del Modelo Económico ---
            # La oferta real de dinero es la oferta nominal (Ms) dividida por el nivel de precios (P).
            Ms_real = Ms / P
            # Se despeja 'i' de la condición de equilibrio Ms/P = kY - hi.
            i_eq = (k * Y - Ms_real) / h

            # --- Subsección 2.2.2: Creación de la Gráfica con Matplotlib ---
            fig, ax = plt.subplots(figsize=(10, 7))
            
            # Se definen rangos FIJOS para los ejes para una visualización estable.
            I_MAX_FIJO = 50
            M_MAX_FIJO = 500
            i_range = np.linspace(0, I_MAX_FIJO, 100)
            
            # Se calcula la Demanda de Dinero (Md) para cada nivel de 'i'.
            Md = k * Y - h * i_range
            
            # Dibujar la curva de Demanda de Dinero (Md).
            ax.plot(Md, i_range, color='orange', linewidth=3, label=f'Demanda de Dinero (Md)')
            # Dibujar la línea vertical de Oferta Real de Dinero (Ms/P).
            ax.axvline(x=Ms_real, color='skyblue', linewidth=3, linestyle='-', label='Oferta Real (Ms/P)')
            # Marcar el punto de equilibrio.
            ax.plot(Ms_real, i_eq, 'o', color='black', markersize=10, label=f'Equilibrio (i={i_eq:.2f})')
            # Añadir línea de guía horizontal desde el equilibrio.
            ax.hlines(i_eq, 0, Ms_real, color='black', linestyle=':', alpha=0.8)

            # --- Subsección 2.2.3: Estilo y Formato de la Gráfica ---
            ax.set_title(f"Tasa de Interés de Equilibrio: {i_eq:.2f}%", fontsize=16)
            ax.set_xlabel("Cantidad Real de Dinero (M/P)", fontsize=12)
            ax.set_ylabel("Tasa de Interés (i)", fontsize=12)
            ax.grid(True, linestyle=':', alpha=0.6)
            ax.legend(loc="upper right")
            
            # Se establecen límites fijos para los ejes.
            ax.set_xlim(left=0, right=M_MAX_FIJO)
            ax.set_ylim(bottom=0, top=I_MAX_FIJO)

            plt.tight_layout()
            plt.show()

    # --- 2.3. Lógica de Interacción (Observadores) ---
    # Esta sección conecta los sliders con la función de dibujo.
    def on_value_change(change):
        # Llama a la función de dibujo con los valores actuales de todos los sliders.
        dibujar_grafica(oferta_slider.value, ingreso_slider.value, precio_slider.value)

    # Se "observa" cada slider; si su 'value' cambia, se llama a 'on_value_change'.
    for slider in [oferta_slider, ingreso_slider, precio_slider]:
        slider.observe(on_value_change, names='value')

    # --- 2.4. Organización y Visualización de la Interfaz de Usuario (UI) ---
    # Se agrupan los widgets de forma ordenada para presentarlos al usuario.
    
    # Se crea una caja vertical para los controles.
    controles = widgets.VBox([
        widgets.VBox([oferta_label, oferta_slider]),
        widgets.VBox([ingreso_label, ingreso_slider]),
        widgets.VBox([precio_label, precio_slider])
    ], layout=widgets.Layout(width='400px'))
    
    # Se combinan los controles (izquierda) y la gráfica (derecha) en una caja horizontal.
    ui = widgets.HBox([controles, plot_output], layout=widgets.Layout(align_items='center'))

    # --- 2.5. Llamada Inicial para Dibujar la Gráfica ---
    # Se llama a la función una vez al principio para que la gráfica aparezca
    # con los valores iniciales de los sliders.
    on_value_change(None)

    # Finalmente, la función devuelve la interfaz completa.
    return ui

# ------------------------------------------------------------------------------
# SECCIÓN 3: EJECUCIÓN Y VISUALIZACIÓN
# ------------------------------------------------------------------------------
# Para mostrar la interfaz interactiva en el cuaderno de Jupyter,
# simplemente llamamos a la función principal.
display(crear_grafica_mercado_dinero())


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

