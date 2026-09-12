/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   compute_disorder.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mkhashan <mkhashan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/28 19:29:05 by mkhashan          #+#    #+#             */
/*   Updated: 2026/01/28 19:29:05 by mkhashan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	idx_val(t_stack *stack_a, int idx)
{
	int		it;
	t_node	*temp;

	it = 0;
	temp = stack_a->head;
	while (it < idx)
	{
		temp = temp->next;
		it++;
	}
	return (temp->val);
}

float	compute_disorder(t_stack *stack_a)
{
	double	mistakes;
	double	total;
	int		it1;
	int		it2;

	mistakes = 0;
	total = 0;
	it1 = 0;
	while (it1 < stack_a->size)
	{
		it2 = it1 + 1;
		while (it2 < stack_a->size)
		{
			if (idx_val(stack_a, it1) > idx_val(stack_a, it2))
			{
				mistakes += 1;
			}
			total += 1;
			it2++;
		}
		it1++;
	}
	return ((float)((float)mistakes / total));
}
