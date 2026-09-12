/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   repair_sort.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mkhashan <mkhashan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/06 06:32:31 by mkhashan          #+#    #+#             */
/*   Updated: 2026/02/06 06:32:31 by mkhashan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	get_min_idx(t_stack *a)
{
	t_node	*tmp;
	int		min;
	int		idx;
	int		min_idx;

	if (!a || !a->head)
		return (-1);
	tmp = a->head;
	min = tmp->val;
	idx = 0;
	min_idx = 0;
	while (idx < a->size)
	{
		if (tmp->val < min)
		{
			min = tmp->val;
			min_idx = idx;
		}
		tmp = tmp->next;
		idx++;
	}
	return (min_idx);
}

static int	get_insert_pos(t_stack *a, int val)
{
	t_node	*tmp;
	int		target_idx;
	int		idx;
	long	best_val;

	tmp = a->head;
	idx = 0;
	target_idx = -1;
	best_val = 2147483648;
	while (idx < a->size)
	{
		if (tmp->val > val && tmp->val < best_val)
		{
			best_val = tmp->val;
			target_idx = idx;
		}
		tmp = tmp->next;
		idx++;
	}
	if (target_idx == -1)
		return (get_min_idx(a));
	return (target_idx);
}

static void	smart_rotate_a(t_stack *a, int index)
{
	int	size;

	size = a->size;
	if (index <= size / 2)
		a_1s(rx, a, "ra", index);
	else
		a_1s(rrx, a, "rra", size - index);
}

static void	filter_stack_a(t_stack *a, t_stack *b)
{
	int	last_valid;
	int	size;
	int	i;

	last_valid = a->head->val;
	a_1s(rx, a, "ra", 1);
	size = a->size;
	i = 1;
	while (i < size)
	{
		if (a->head->val > last_valid)
		{
			last_valid = a->head->val;
			a_1s(rx, a, "ra", 1);
		}
		else
			a_2s(a, b, "pb", 1);
		i++;
	}
}

void	repair_sort(t_stack *a, t_stack *b)
{
	int	target;

	smart_rotate_a(a, get_min_idx(a));
	if (is_sorted(a))
		return ;
	filter_stack_a(a, b);
	while (b->size > 0)
	{
		target = get_insert_pos(a, b->head->val);
		smart_rotate_a(a, target);
		a_2s(b, a, "pa", 1);
	}
	smart_rotate_a(a, get_min_idx(a));
}
