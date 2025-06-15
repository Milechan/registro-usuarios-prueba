import { useRef } from "react"

const Register = () => {

    const name = useRef(null)
    const email = useRef(null)
    const password = useRef(null)

    const validate = () => {
        if (name.current.value == "" || email.current.value == "" || password.current.value == "") {
            return false
        }
        const emailRegex = new RegExp("^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$")
        if (!emailRegex.test(email.current.value)) {
            return false
        }
        if (password.current.value.length < 6) {
            return false
        }
        return true
    }

    
    return (
        <div className="container-Register">
            <div className="mb-3">
                <label for="Input1" className="form-label">Nombre Completo</label>
                <input ref={name} type="text" className="form-control" id="Input1" placeholder="Escribe Tu Nombre" />
            </div>
            <div className="mb-3">
                <label for="Input2" className="form-label">Correo electronico</label>
                <input ref={email} type="email" className="form-control" id="Input2" placeholder="Escribe Tu Correo" />
            </div>
            <div className="mb-3">
                <label for="Input3" className="form-label">Contraseña</label>
                <input ref={password} type="text" className="form-control" id="Input3" placeholder="Crea Tu Contraseña" />
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