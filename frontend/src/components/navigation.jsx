import Link from 'next/link'


import styles from './navigation.module.css'

const menuLinks = [
    {
        label: 'Inicio',
        route: '/'
    },
    {
        label: 'Pedidos',
        route: '/pedidos'
    },
    {
        label: 'Nuevo Pedido',
        route: '/pedidos/nuevopedido'
    },
    {
        label: 'Clientes',
        route: '/clientes'
    },
    {
        label: 'Nuevo Cliente',
        route: '/clientes/nuevocliente'
    },
]


export function Navigation() {
    return (
        <nav className="bg-gray-800 mb-2">
            <div className="max-w-7xl mx-auto px-2 sm:px-6 lg:px-8">
                <div className="relative flex items-center justify-center h-16">
                    <div className="sm:block sm:ml-6">
                        <div className="flex space-x-4 items-center">
                            {menuLinks.map((link, index) => (
                                <Link key={index} href={link.route} className="text-gray-300 hover:bg-gray-700 px-3 py-2 rounded-md text-sm font-medium">
                                        {link.label}
                                </Link>
                            ))}
                        </div>
                    </div>
                </div>
            </div>
        </nav>
    )
}