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
		PyObject *item = PyList_GetItem(p, i);
		PyObject *item_type = PyObject_Type(item);
		PyObject *item_bytes = PyObject_Str(item_type);
		char *type_str = PyUnicode_AsUTF8(item_bytes);
		Py_ssize_t type_length = PyUnicode_GET_LENGTH(item_bytes);

		printf("Element %zd: %s\n", i, type_str);

		if (PyBytes_Check(item))
			print_python_bytes(item);

		Py_DECREF(item_type);
		Py_DECREF(item_bytes);
		Py_DECREF(item);
	}
}

/**
 * print_python_bytes - Prints basic information about a Python bytes object.
 * @p: Pointer to the Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", str);

	printf("  first %zd bytes:", size + 1 > 10 ? 10 : size + 1);
	for (i = 0; i < size + 1 && i < 10; i++)
		printf(" %02hhx", str[i]);
	printf("\n");
}
