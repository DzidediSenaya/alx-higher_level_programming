#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic information about a
 * Python list object.
 *
 * @param p: Pointer to the Python list object.
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = ((PyListObject *)p)->ob_item[i];
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}


/**
 * print_python_bytes - Prints basic information about a
 * Python bytes object.
 *
 * @param p Pointer to the Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    unsigned char *bytes;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyObject_Length(p);
    bytes = (unsigned char *)PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyUnicode_AsUTF8(p));
    printf("  first %d bytes:", size < 10 ? (int)size : 10);
    for (i = 0; i < (size < 10 ? size : 10); i++)
    {
        printf(" %02x", bytes[i]);
    }
    printf("\n");
}

/**
 * print_python_float - Prints basic information about a
 * Python float object.
 *
 * @param p Pointer to the Python float object.
 */
void print_python_float(PyObject *p)
{
    double value;

    printf("[.] float object info\n");

    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    value = PyFloat_AS_DOUBLE(p);
    printf("  value: %f\n", value);
}

