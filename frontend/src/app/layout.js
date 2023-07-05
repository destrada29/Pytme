import { Navigation } from '@/components/navigation'

import './styles/globals.css'

import { Inter } from 'next/font/google'



const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'Inicio',
  description: 'Prueba técnica PymeDesk',
}



export default function RootLayout({ children }) {
  return (
    <html lang="es-co">
      <head>
        <title></title>
      </head>
      <body className={inter.className}>
        <header>
          <Navigation />
        </header>
        {children}
      </body>
    </html>
  )
}
