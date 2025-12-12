from pathlib import Path
import csv
from datetime import datetime


def save_fig(fig, name, fig_dir=Path('../figures'), dpi=300, ext='png', description='', generator='script', source='', params=''):
    """Guarda una figura matplotlib y registra una entrada en figures/manifest.csv.

    Args:
        fig: matplotlib.figure.Figure
        name: nombre base (sin extensión) para el archivo
        fig_dir: ruta al directorio de figuras (relativa al script/notebook)
        dpi: resolución para PNG
        ext: extensión/format (png, svg, pdf)
        description: breve descripción de la figura
        generator: 'notebook' o 'script'
        source: ruta del notebook o script generador
        params: cadena con parámetros importantes (ej: bins=50)

    Returns:
        Path al archivo guardado
    """
    fig_dir = Path(fig_dir)
    fig_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{name}.{ext}"
    path = fig_dir / filename
    fig.savefig(path, dpi=dpi, bbox_inches='tight')

    manifest = fig_dir / 'manifest.csv'
    header = ['filename', 'date_iso', 'description', 'generator', 'source', 'params', 'dpi', 'path']
    exists = manifest.exists()
    with manifest.open('a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow(header)
        writer.writerow([filename, datetime.utcnow().date().isoformat(), description, generator, source, params, dpi, str(path)])

    return path
