#include "lists.h"

void print_python_list_info(PyObject *p)
{
	int k;0
	long int size = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (k = 0; k < size; k++)
		printf("Element %i: %s\n", k, py_TYPE(obj->ob_item[k])->tp_name);
}
