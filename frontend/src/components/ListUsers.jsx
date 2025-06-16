import { useEffect, useState } from "react"
import { useNavigate } from "react-router"
import "../styles/listusers.css"

const ListUsers = () => { //se crea el componente lista de usuarios
    const [listUsers,setListUsers]=useState([])//se crea estado para guardar lista de usuarios
    const navigate = useNavigate()//se define funcion para navegar
    useEffect(() => {//se ejecutara al montar el componente
        const getUsers = async () => {//se define funcion asincrona que obtiene la lista de usuarios de la api
            try {
                const request = await fetch("http://localhost:5000/listusers", {//se realiza el fetch para obtener la informacion de la lista de usuarios desde la api
                    method: "GET",

                })
                const data = await request.json()//obtenemos la respuesta json de la api
                console.log(data)
                if (request.status != 200) {//validamos que el estado de la peticion sea 200(que este ok)
                    console.log("hubo un error al ver la lista de usuarios")
                }
                console.log("la peticion fue exitosa")
                setListUsers(data.users)//se guarda en el estado la respuesta de la api
            } catch (error) {
                console.error(error)
            }
        }
        getUsers()
    }, [])
    return (
        <div className="container-list">
            <h1 className="title"> ✨Lista de Usuarios Registrados✨</h1>
            <ul className="container-user-list">
                {/* para la lista de usuarios retornaremos un LI por cada elemento de la lista */}
                {listUsers.map((user)=>{
                    return <li>({user.full_name}) ({user.email})</li>
                })}
                {/* en caso en que la lista de usuarios este vacia,se mostrara el mensaje */}
              {listUsers.length==0?<div>no se encontraron usuarios</div>:""}  
            </ul>
            <div onClick={() => navigate("/")} className="btn btn-custom-list"> Volver al registro
            </div>
        </div>
    )
}

export default ListUsers