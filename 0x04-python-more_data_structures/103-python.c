#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints basic information about a Python list.
 * @p: Pointer to the Python list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GET_ITEM(p, i);
		PyObject *item_type = Py_TYPE(item);
		PyObject *item_bytes = PyObject_Str(item_type);
		PyObject *item_bytes_encoded = PyUnicode_AsUTF8String(item_bytes);
		char *type_str = PyBytes_AsUTF8(item_bytes_encoded);

		printf("Element %zd: %s\n", i, type_str);

		if (PyBytes_Check(item))
			print_python_bytes(item);

		Py_XDECREF(item);
		Py_XDECREF(item_type);
		Py_XDECREF(item_bytes);
		Py_XDECREF(item_bytes_encoded);
	}
}

/**
 * print_python_bytes - Prints basic information about a Python bytes object.
 * @p: Pointer to the Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	Py_ssize_t max_size = 10;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsUTF8AndSize(p, &str, &size);

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", str);

	printf("  first %zd bytes:", size < max_size ? size + 1 : max_size);
	for (i = 0; i < size && i < max_size; i++)
		printf(" %02hhx", str[i]);
	printf("\n");
}

