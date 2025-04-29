using System;

class Program
{
    static void Main()
    {
        // Definir los vectores de 200 elementos (ejemplo con menos datos)
        int[] VecLegajo = { 100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300 };
        int[] VecNotas =  {  8,   5,   9,   7,   6,   4,   9,   7,   3,   6,   8,   10 };

        // Variables para cálculos
        int sumaNotas100 = 0, cantidad100 = 0;
        int notasAprobadas200 = 0, totalNotas200 = 0;
        int mayorNota300 = -1; // Iniciar con un valor bajo

        // Recorrer los vectores con un bucle
        for (int i = 0; i < VecLegajo.Length; i++)
        {
            int legajo = VecLegajo[i];
            int nota = VecNotas[i];

            // Calcular promedio del legajo 100
            if (legajo == 100)
            {
                sumaNotas100 += nota;
                cantidad100++;
            }

            // Calcular porcentaje de aprobadas del legajo 200
            if (legajo == 200)
            {
                totalNotas200++;
                if (nota >= 6)
                {
                    notasAprobadas200++;
                    //notasAprobadas200 = 3
                }
            }

            // Calcular mayor nota del legajo 300
            if (legajo == 300)
            {
                if (nota > mayorNota300)
                {
                    mayorNota300 = nota;
                }
            }
        }

        // Mostrar resultados
        if (cantidad100 > 0)
        {
            double promedio = (double)sumaNotas100 / cantidad100;
            Console.WriteLine("El promedio de calificaciones del legajo 100 es: " + promedio);
        }
        else
        {
            Console.WriteLine("No se encontraron notas para el legajo 100.");
        }

        if (totalNotas200 > 0)
        {
            double porcentajeAprobadas = (double)notasAprobadas200 / totalNotas200 * 100;
            //porcentajeAprobadas = 75%
            Console.WriteLine("El porcentaje de notas aprobadas del legajo 200 es: " + porcentajeAprobadas + "%");
        }
        else
        {
            Console.WriteLine("No se encontraron notas para el legajo 200.");
        }

        if (mayorNota300 != -1)
        {
            Console.WriteLine("La mayor nota del legajo 300 es: " + mayorNota300);
        }
        else
        {
            Console.WriteLine("No se encontraron notas para el legajo 300.");
        }
    }
}
