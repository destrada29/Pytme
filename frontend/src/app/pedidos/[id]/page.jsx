export default async function GetClientePage({ params }) {
    const { id } = params
  
    const fetchClienteID = () => {
      return fetch(`http://127.0.0.1:8000/pedidos/${id}/`)
        .then(response => response.json())
    }
  
    const res = await fetchClienteID()
  
    console.log(res)
    
    return (
        <ul>
          {Object.entries(res).map(([key, value]) => (
            <li key={key}>
              <strong>{key}: </strong>
              {typeof value === 'object' ? (
                <ul>
                  {Object.entries(value).map(([subKey, subValue]) => (
                    <li key={subKey}>
                      <strong>{subKey}: </strong>
                      {subValue}
                    </li>
                  ))}
                </ul>
              ) : (
                value
              )}
            </li>
          ))}
        </ul>
      )
  }
  