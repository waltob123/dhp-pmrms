from health_app.utils.constants import PAGE, PAGE_SIZE


def filter_sort_processor(*, filters_or_sort_param: list) -> dict:
    """
    Process the filters and sort for the query.

    :param filters_or_sort_param: The filters or sort parameters.
    :return: The processed filters as a dictionary.
    """
    results = {}
    for item in filters_or_sort_param:
        try:
            key, value = item.split("=")
        except ValueError:
            continue

        # Convert numeric values to integers
        if value.isdigit():
            value = int(value)

        # Handle duplicate keys
        if key in results:
            if isinstance(results[key], list):
                results[key].append(value)
            else:
                results[key] = [results[key], value]
        else:
            results[key] = value

    return results


def set_filter_defaults(filters: dict) -> dict:
    """
    Set the page and page size if they are not provided

    :param filters: The filters to apply
    :return: The updated filters
    """

    if "page" not in filters:
        filters["page"] = PAGE

    if "page_size" not in filters:
        filters["page_size"] = PAGE_SIZE

    if "is_deleted" not in filters:
        filters["is_deleted"] = False

    return filters
