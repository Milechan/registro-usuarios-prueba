const Register = () => {
    return (
        <div className="container-Register">
            <div className="mb-3">
                <label for="Input1" className="form-label">Nombre Completo</label>
                <input type="text" className="form-control" id="Input1" placeholder="Escribe Tu Nombre"/>
            </div>
            <div className="mb-3">
                <label for="Input2" className="form-label">Correo electronico</label>
                <input type="email" className="form-control" id="Input2" placeholder="Escribe Tu Correo"/>
            </div>
            <div className="mb-3">
                <label for="Input3" className="form-label">Contraseña</label>
                <input type="text" className="form-control" id="Input3" placeholder="Crea Tu Contraseña"/>
            </div>

            <div className="button-container">
                <div className="btn btn-primary">Registrar</div>
            </div>
            <div className="button-container">
                <div className="btn btn-primary">Lista de Usuarios Registrados</div>
            </div>
        </div>
    )
}

export default Register