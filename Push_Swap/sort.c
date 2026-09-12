/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mkhashan <mkhashan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/29 14:28:48 by mkhashan          #+#    #+#             */
/*   Updated: 2026/01/29 14:28:48 by mkhashan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	clear_stacks(t_stack *stack_a, t_stack *stack_b)
{
	clear_stack(stack_a);
	clear_stack(stack_b);
}

void	adaptive(t_stack *stack_a, t_stack *stack_b, float disorder)
{
	if (stack_a->size <= 5)
		tiny_sort(stack_a, stack_b);
	else if (disorder < 0.2)
		repair_sort(stack_a, stack_b);
	else if (disorder < 0.5)
		m_sort(stack_a, stack_b);
	else
		c_sort(stack_a, stack_b);
}

void	start_sort(t_stack *stack_a, t_config *conf)
{
	float	dis_ordered;
	t_stack	*stack_b;

	dis_ordered = compute_disorder(stack_a);
	stack_b = stack_create();
	if (conf->mod == 0)
		s_sort(stack_a, stack_b);
	else if (conf->mod == 1)
		m_sort(stack_a, stack_b);
	else if (conf->mod == 2)
		c_sort(stack_a, stack_b);
	else
		adaptive(stack_a, stack_b, dis_ordered);
	if (conf->bench)
		bench(stack_a, stack_b, conf, dis_ordered);
	clear_stacks(stack_a, stack_b);
}
