'use client'
import { useEffect, useState } from "react";

export default function ListData(url) {
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(url);
                const res = await response.json();
                setData(res.results);
            } catch (error) {
                console.error("Error fetching data: ", error);
            }
        };

        fetchData();
    }, [url]);

    return data;
}