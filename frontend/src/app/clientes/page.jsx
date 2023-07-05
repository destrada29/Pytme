import Link from 'next/link'

const fetchListaClientes = () => {
  const data = fetch(`http://127.0.0.1:8000/usuarios/listar/`)
    .then(response => response.json())
  return data
}

const res = await fetchListaClientes()

const table_menu = [
  {
    th: "ID"
  },
  {
    th: "Nombres",
  },
  {
    th: "Apellidos",
  },
  {
    th: "Usuario",
  },
  {
    th: "Correo",
  },
  {
    th: "Celular",
  },
  {
    th: "Ciudad",
  },
  {
    th: "Dirección"
  },
  {
    th: "Ver"
  }
]

export default async function ListarClientesPage() {

  return (
    <table className="table-auto border-separate border-spacing-2">
      <thead>
        <tr>
          {table_menu.map(({ th }) => (
            <th>{th}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {res.results.map((item) => (
          <tr key={item.id}>
            <td>{item.id}</td>
            <td>{item.first_name}</td>
            <td>{item.last_name}</td>
            <td>{item.username}</td>
            <td>{item.email}</td>
            <td>{item.phone}</td>
            <td>{item.city}</td>
            <td>{item.address}</td>
            <td>
              <Link key={item.id} href="/clientes/[id]" as={`/clientes/${item.id}`} className='bg-sky-500 hover:bg-sky-700' type='button'>
                Ver
              </Link>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  )
}
