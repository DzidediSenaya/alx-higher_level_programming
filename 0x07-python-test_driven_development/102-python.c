#include <Python.h>

/**
 * print_python_string - Prints information about Python strings
 * @p: Python object (string)
 */
void print_python_string(PyObject *p)
{
	PyObject *str_bytes;
	const char *type;

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		type = "compact ascii";
	else if (PyUnicode_IS_COMPACT(p))
		type = "compact unicode object";
	else
		type = "unicode object";

	printf("  type: %s\n", type);
	printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));

	str_bytes = PyUnicode_AsUTF8String(p);
	printf("  value: %s\n", PyBytes_AsString(str_bytes));

	Py_DECREF(str_bytes);
}

