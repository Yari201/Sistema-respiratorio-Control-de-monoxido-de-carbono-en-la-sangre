[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=Yari201/Sistema-respiratorio-Control-de-monoxido-de-carbono-en-la-sangre)

# Control de monóxido de carbono en sangre

## Estudiantes
Escobedo Tellez Yadhira Lisset;Gonzalez Morales Fabian;Hernandez Peraza Paola Giselle;Zabala Silva Rosa Helena
Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México. Email: yadhira.escobedo201@tectijuana.edu.mx;fabian.gonzalez193@tectijuana.edu.mx;paola.hernandez19@tectijuana.edu.mx;rosa.zavala201@tectijuana.edu.mx

## Asignaturas o departamento donde se puede usar la Actividad
Modelado de Sistemas Fisiológicos de Ingeniería Biomédica

## Información general
El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivo general
Diseñar un gemelo digital de un sistema fisiológico que permita identificar las diferencias entre un paciente afectado por una enfermedad (caso) y un individuo saludable (control) para desarrollar un protocolo de tratamiento mediante un sistema de control en lazo cerrado.

## Descripción detallada del sistema
La mayoría de los accidentes causados por envenenamiento por monóxido de carbono (CO) se producen en los hogares y están relacionados a nuestras actividades diarias como cocinar y usar la calefacción. Debido a que el CO es un gas "invisible y silencioso" sus características no nos permiten, en muchos casos, que nos demos cuenta del peligro que éste presenta, resultando en envenenamiento por inhalación en cuestión de minutos.

Dentro del sistema respiratorio, las vías respiratorias son divididas en dos categorías las cuales cuentan con resistencias mecánicas al fluido representadas por RC, que representa las vías respiratorias superiores que constan de nariz, cavidad nasal, faringe y laringe; y RP que se compone de las vías respiratorias inferiores que son la tráquea, bronquios y alvéolos, respectivamente. El efecto de la inercia al flujo de gas en las vías respiratorias centrales está dado por LC. El aire que ingresa a los alvéolos también produce una expansión de la cavidad de la pared torácica con el mismo volumen. Esto está representado por la conexión de las conformidades pulmonares (CL) y CM representando la liberación de CO a los tejidos en partes por millón. 

A la entrada del sistema se observa una señal sinusoidal representativa del ciclo de inhalación y exhalación. Las presiones desarrolladas en el modelo pulmonar son Pao(t) en la apertura de la vía aérea pulmonar, PA (t) en los alvéolos.  El caudal volumétrico de aire que ingresa al sistema respiratorio está dado por Q(t) y el flujo entregado a los alvéolos por QA (t). Por lo tanto, el flujo derivado de los alvéolos debe ser Q(t) - QA (t). 

## Referencias principales
[1] H. Motulsky, Intuitive biostatistics: a nonmathematical guide to statistical thinking. 4th ed. Oxford, New York, USA: Oxford University Press, 2014.

[2] P. A. Valle, L. N. Coria, C. Plata & Y. Salazar, “CAR-T cell therapy for the treatment of ALL: eradication conditions and in silico experimentation,” Hemato, vol. 2, issue 3, pp. 441-462, Jul 2021. https://doi.org/10.3390/hemato2030028 

[3] MathWorks. (n.d.). Sistemas Dinámicos [Online]. Available: https://www.mathworks.com/discovery/dynamic-systems.html

