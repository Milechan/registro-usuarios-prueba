import { useNavigate } from "react-router"

const ListUsers = () => {
    const navigate = useNavigate()
    return (
        <div>
            <h1>Lista de Usuarios Registrados</h1>
            <ul className="container-list">
                <li>(nombre de usuario) (correo)</li>
            </ul>
            <div onClick={() => navigate("/")} className="btn btn-primary"> Volver al registro
            </div>
        </div>
    )
}

export default ListUsers