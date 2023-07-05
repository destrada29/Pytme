function Metric({ label, value }) {
    return (
        <div className="p-4 bg-gray-200 rounded-lg shadow-md">
            <div className="text-sm text-gray-500">{label}</div>
            <div className="text-3xl font-bold">{value}</div>
        </div>
    );
}

export default async function Metrics() {


    const fetchResume = () => {
        return fetch('http://127.0.0.1:8000/resumen/', {next: {revalidate:10}})
            .then(response => response.json())
    }

    const res = await fetchResume()

    if (!res) {
        return <div>Cargando datos...</div>;
    }

    return (
        <div className="grid grid-cols-2 gap-4">
            <Metric label="Número de pedidos" value={res.num_orders} />
            <Metric label="Número de clientes" value={res.num_customers} />
            <Metric label="Ingresos del último mes" value={`$${res.income_last_month}`} />
            <Metric label="Ingresos de este mes" value={`$${res.income_current_month}`} />
            <Metric label="Ciudad con más pedidos" value={res.city_more_orders} />
            <Metric label="Producto más vendido" value={res.best_selling_product} />
        </div>
    )
}
