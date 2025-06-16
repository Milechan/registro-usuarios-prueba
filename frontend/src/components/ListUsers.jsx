import { useEffect, useState } from "react"
import { useNavigate } from "react-router"

const ListUsers = () => {
    const [listUsers,setListUsers]=useState([])
    const navigate = useNavigate()
    useEffect(() => {
        const getUsers = async () => {
            try {
                const request = await fetch("http://localhost:5000/listusers", {
                    method: "GET",

                })
                const data = await request.json()
                console.log(data)
                if (request.status != 200) {
                    console.log("hubo un error al ver la lista de usuarios")
                }
                console.log("la peticion fue exitosa")
                setListUsers(data.users)
            } catch (error) {
                console.error(error)
            }
        }
        getUsers()
    }, [])
    return (
        <div>
            <h1>Lista de Usuarios Registrados</h1>
            <ul className="container-list">
                {listUsers.map((user)=>{
                    return <li>({user.full_name}) ({user.email})</li>
                })}
              {listUsers.length==0?<div>no se encontraron usuarios</div>:""}  
            </ul>
            <div onClick={() => navigate("/")} className="btn btn-primary"> Volver al registro
            </div>
        </div>
    )
}

export default ListUsers