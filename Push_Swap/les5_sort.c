/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   les5_sort.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mkhashan <mkhashan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/06 06:22:49 by mkhashan          #+#    #+#             */
/*   Updated: 2026/02/06 06:22:49 by mkhashan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	get_min_pos(t_stack *a)
{
	t_node	*temp;
	int		min;
	int		min_pos;
	int		i;

	temp = a->head;
	min = temp->val;
	min_pos = 0;
	i = 0;
	while (i < a->size)
	{
		if (temp->val < min)
		{
			min = temp->val;
			min_pos = i;
		}
		temp = temp->next;
		i++;
	}
	return (min_pos);
}

void	sort_three(t_stack *a)
{
	int	first;
	int	second;
	int	third;

	if (a->size != 3)
		return ;
	first = a->head->val;
	second = a->head->next->val;
	third = a->head->next->next->val;
	if (first > second && second > third)
	{
		a_1s(sx, a, "sa", 1);
		a_1s(rrx, a, "rra", 1);
	}
	else if (first > second && third > second && first > third)
		a_1s(rx, a, "ra", 1);
	else if (first > second && second < third && first < third)
		a_1s(sx, a, "sa", 1);
	else if (first < second && second > third && first < third)
	{
		a_1s(sx, a, "sa", 1);
		a_1s(rx, a, "ra", 1);
	}
	else if (first < second && second > third && first > third)
		a_1s(rrx, a, "rra", 1);
}

void	sort_five(t_stack *a, t_stack *b)
{
	int	min_pos;

	while (a->size > 3)
	{
		min_pos = get_min_pos(a);
		if (min_pos <= a->size / 2)
			while (min_pos-- > 0)
				a_1s(rx, a, "ra", 1);
		else
			while (min_pos++ < a->size)
				a_1s(rrx, a, "rra", 1);
		a_2s(a, b, "pb", 1);
	}
	sort_three(a);
	while (b->size > 0)
		a_2s(b, a, "pa", 1);
}

void	tiny_sort(t_stack *a, t_stack *b)
{
	if (a->size == 2)
	{
		if (a->head->val > a->head->next->val)
			a_1s(sx, a, "sa", 1);
	}
	else if (a->size == 3)
		sort_three(a);
	else
		sort_five(a, b);
}
