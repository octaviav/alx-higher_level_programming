#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int siz = PyList_Size(p);
	int k;
	PyListObject *object = (PyListObject *)p;

	printf("[*] Size of the Python Ist = %li\n", siz);
	printf("[*] Allocated = %li\n", object->allocated);
	for (k = 0; k < siz; k++)
		printf("Element %i: %s\n", k, py_TYPE(object->ob_item[k])->tp_name);
}
