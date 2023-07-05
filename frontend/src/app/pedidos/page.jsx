'use client'
import React, { useEffect, useState } from "react";

const fetchListaPedidos = async () => {
  const response = await fetch(`http://127.0.0.1:8000/pedidos/`);
  const data = await response.json();
  return data.results;
};

export default function ListarPedidosPage() {
  const [pedidos, setPedidos] = useState([]);

  useEffect(() => {
    const obtenerPedidos = async () => {
      const listaPedidos = await fetchListaPedidos();
      setPedidos(listaPedidos);
    };

    obtenerPedidos();
  }, []);

  return (
    <table className="table-auto border-separate border-spacing-2">
      <thead>
        <tr>
          <th>ID</th>
          <th>Producto</th>
          <th>Descripción</th>
          <th>Pedido</th>
          <th>Cantidad</th>
          <th>Precio</th>
          <th>Total</th>
        </tr>
      </thead>
      <tbody>
        {pedidos.map((pedido) => (
          <tr key={pedido.id}>
            <td>{pedido.id}</td>
            <td>{pedido.product.name}</td>
            <td>{pedido.product.description}</td>
            <td>{pedido.product_order}</td>
            <td>{pedido.amount}</td>
            <td>{pedido.product.price}</td>
            <td>{pedido.amount * pedido.product.price}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
