/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   bucket_sort_utlis.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mkhashan <mkhashan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/29 14:26:28 by mkhashan          #+#    #+#             */
/*   Updated: 2026/01/29 14:26:28 by mkhashan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	s_init_sort(int *arr, int size)
{
	int	it;
	int	temp;

	while (size)
	{
		it = 1;
		while (it < size)
		{
			if (arr[it] < arr[it - 1])
			{
				temp = arr[it - 1];
				arr[it - 1] = arr[it];
				arr[it] = temp;
			}
			it++;
		}
		size--;
	}
}

static void	map_val(t_stack *stack_a, int *arr)
{
	t_node	*temp;
	int		it1;
	int		it2;

	it1 = 0;
	it2 = 0;
	temp = stack_a->head;
	while (it1 < stack_a->size)
	{
		it2 = 0;
		while (temp->val != arr[it2])
			it2++;
		temp->val = it2;
		temp = temp->next;
		it1++;
	}
}

static void	indexer(t_stack *stack_a)
{
	int		*arr_num;
	t_node	*temp;
	int		it;

	arr_num = malloc(sizeof(int) * stack_a->size);
	if (!arr_num)
		exit(1);
	it = 0;
	temp = stack_a->head;
	while (it < stack_a->size)
	{
		arr_num[it] = temp->val;
		temp = temp->next;
		it++;
	}
	s_init_sort(arr_num, stack_a->size);
	map_val(stack_a, arr_num);
	free(arr_num);
}

void	f_p_s(t_stack *stack_a, t_stack *stack_b)
{
	int	it;
	int	bucket_n;
	int	chunk;
	int	size_snapshot;

	bucket_n = 1;
	chunk = (stack_a->size / 11) + 1;
	if (stack_a->size <= 100)
		chunk = (stack_a->size / 5) + 1;
	while (stack_a->head)
	{
		it = 0;
		size_snapshot = stack_a->size;
		while (it < size_snapshot && stack_a->head)
		{
			if (stack_a->head->val < chunk * bucket_n)
				a_2s(stack_a, stack_b, "pb", 1);
			else
				a_1s(rx, stack_a, "ra", 1);
			it++;
		}
		bucket_n++;
	}
}

void	m_sort(t_stack *stack_a, t_stack *stack_b)
{
	int	dis;

	indexer(stack_a);
	f_p_s(stack_a, stack_b);
	while (stack_b->size)
	{
		dis = d(stack_b, stack_b->size - 1);
		if (dis > 0)
			a_1s(rx, stack_b, "rb", dis);
		else if (dis < 0)
			a_1s(rrx, stack_b, "rrb", -1 * dis);
		a_2s(stack_b, stack_a, "pa", 1);
	}
}
