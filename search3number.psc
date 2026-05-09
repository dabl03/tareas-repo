Proceso search3number
	Definir x, y_, z Como Real;
	Definir is_squal Como Logico;
	Escribir "Buscador de numero mas cercano a 10.";
	Escribir "Ingrese 3 numeros para darle valor a x, y, z.";
	Escribir "x?" Sin Saltar;
	// Sin saltar es un operador que indica a escribir que no coloque saltos de linea
	Leer x;
	Escribir "y? " Sin Saltar;
	Leer y_;
	Escribir "z? " Sin Saltar;
	Leer z;
	
	// Sacamos la diferencia.
	x<-abs(10-x);// ABS convierte los negativos a positivos, y deja igual a los positivos.
	y_<-abs(10-y_);
	z<-abs(10-z);
	is_squal<-x=0 o y_=0 o z=0;// Para dar un mensaje de numeros iguales a 0
	
	Si is_squal Entonces
		// Ahora la usaremos para ver si se coloca ",".
		is_squal<-Falso;
		Escribir "Las variables iguales a 10 son: " Sin Saltar;
		
		Si x=0 Entonces
			Escribir "x" Sin Saltar;
			is_squal<-Verdadero;
		FinSi
		SI y_=0 Entonces
			Si is_squal Entonces
				Escribir ", " Sin Saltar;
			FinSi
			Escribir "y" Sin Saltar;
			is_squal<-Verdadero;
		FinSi
		Si z=0 Entonces
			Si is_squal Entonces
				Escribir ", " Sin Saltar;
			FinSi
			Escribir "z";
		FinSi
	FinSi
	// Si su valor fué 10 entonces no mostramos si se acerca mas a 10.
	Si x<>0 Entonces
		// Primero debemos comprobar si x es igual a otra variables.
		Si x=y_ y x<z Entonces
			Escribir "x he y son mas cercanos a 10";
		SiNo
			Si x=z y x<y_ Entonces
				Escribir "X he z son mas cercanos a 10";
			SiNo
				// Ya comprobamos si x es igual a otra variable.
				// Ahora debemos comprobar si es menor a las demas.
				Si x<y_ y x<z Entonces
					Escribir "X es la variable mas cercana a 10";
				FinSi
			FinSi
		FinSi
	FinSi
	
	Si y_<>0 Entonces
		Si y_=z y y_<x Entonces
			Escribir "Z he y Son mas cercanos a 10.";
		SiNo
			// Ya comprobamos si y es igual a x.
			// Comprobemos directamente si es menor a los demas.
			Si y_<z y y_<x Entonces
				Escribir "Y es la variable mas cercana a 10";
			// SiNo
				// Escribir "Z es la variable mas cercana a 10";
				// Este codigo no funcionaria si y fuera igual a 10.
			FinSi
		FinSi
	FinSi
	
	Si z<>0 y z<x y z<y_ Entonces
		// ya comprobamos las igualdades.
		Escribir "Z es la variable mas cercana a 10";
	SiNo
		Si z<>0 y z=x y z=y_ Entonces
			// Me falto ver si todas son iguales xD
			Escribir "Todas valen lo mismo, la distancia que tienen de 10 es: ",z," km";
		FinSi
	FinSi
FinProceso
