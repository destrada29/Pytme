export default async function GetClientePage({ params }) {
  const { id } = params

  const fetchClienteID = () => {
    return fetch(`http://127.0.0.1:8000/usuarios/${id}/`)
      .then(response => response.json())
  }

  const res = await fetchClienteID()

  return (
    <main className="">
      <ul>
        {Object.entries(res).map(([key, value]) => (
          <li key={key}>
            <strong>{key}: </strong>
            {typeof value === 'object' || typeof value === 'boolean' ? JSON.stringify(value) : value}
          </li>
        ))}
      </ul>
    </main>
  )
}
