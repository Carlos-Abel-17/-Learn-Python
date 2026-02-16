"""
Módulo semilla: crea la estructura inicial de carpetas y archivos de recetas.
"""
from pathlib import Path


def crear_estructura_inicial(ruta_base):
    """
    Función semilla que crea la estructura inicial de carpetas y archivos
    según la estructura definida (Carnes, Ensaladas, Pastas, Postres).
    """
    estructura = {
        "Carnes": [
            ("Etrecot al Malbec.txt", "Receta de Etrecot al Malbec\n\nIngredientes:\n- Entrecot de res\n- Vino Malbec\n- Hierbas aromáticas\n\nPreparación:\n[Tu receta aquí]"),
            ("Matambre a la Pizza.txt", "Receta de Matambre a la Pizza\n\nIngredientes:\n- Matambre\n- Salsa de tomate\n- Queso mozzarella\n- Orégano\n\nPreparación:\n[Tu receta aquí]")
        ],
        "Ensaladas": [
            ("Ensalada Griega.txt", "Receta de Ensalada Griega\n\nIngredientes:\n- Tomates\n- Pepino\n- Aceitunas\n- Queso feta\n- Aceite de oliva\n\nPreparación:\n[Tu receta aquí]"),
            ("Ensalada Mediterranea.txt", "Receta de Ensalada Mediterránea\n\nIngredientes:\n- Lechuga\n- Tomates cherry\n- Aceitunas\n- Queso de cabra\n- Vinagreta\n\nPreparación:\n[Tu receta aquí]")
        ],
        "Pastas": [
            ("Canelones de Espinaca.txt", "Receta de Canelones de Espinaca\n\nIngredientes:\n- Pasta para canelones\n- Espinaca\n- Ricotta\n- Salsa bechamel\n\nPreparación:\n[Tu receta aquí]"),
            ("Ravioles de Ricotta.txt", "Receta de Ravioles de Ricotta\n\nIngredientes:\n- Masa para ravioles\n- Ricotta\n- Espinaca\n- Salsa de tomate\n\nPreparación:\n[Tu receta aquí]")
        ],
        "Postres": [
            ("Compota de Manzana.txt", "Receta de Compota de Manzana\n\nIngredientes:\n- Manzanas\n- Azúcar\n- Canela\n- Agua\n\nPreparación:\n[Tu receta aquí]"),
            ("Tarta de Frambuesa.txt", "Receta de Tarta de Frambuesa\n\nIngredientes:\n- Frambuesas\n- Masa quebrada\n- Crema pastelera\n- Azúcar\n\nPreparación:\n[Tu receta aquí]")
        ]
    }

    for categoria, recetas in estructura.items():
        ruta_categoria = Path(ruta_base, categoria)

        if not ruta_categoria.exists():
            ruta_categoria.mkdir(parents=True, exist_ok=True)
            print(f'✓ Categoría "{categoria}" creada')

        for nombre_archivo, contenido in recetas:
            ruta_archivo = Path(ruta_categoria, nombre_archivo)
            if not ruta_archivo.exists():
                ruta_archivo.write_text(contenido, encoding='utf-8')
                print(f'  ✓ Receta "{nombre_archivo}" creada')

    print(f'\n✓ Estructura inicial creada exitosamente en: {ruta_base}')
