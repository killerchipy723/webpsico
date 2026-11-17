from flask import Blueprint, render_template, request, redirect, url_for, flash

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/contacto', methods=['POST'])
def contacto():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    telefono = request.form.get('telefono')
    motivo = request.form.get('motivo')
    
    # Lógica de guardado o notificación
    flash(f'¡Gracias {nombre}! Tu solicitud ha sido enviada con éxito.', 'success')
    return redirect(url_for('main.index') + '#contacto')