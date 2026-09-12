/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   bench.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mkhashan <mkhashan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/05 08:48:02 by mkhashan          #+#    #+#             */
/*   Updated: 2026/02/05 08:48:02 by mkhashan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

char	*check_mod(float dis_order)
{
	if (dis_order < 0.2)
		return ("O(n)");
	else if (dis_order < 0.5)
		return ("O(n√n)");
	else
		return ("O(nlogn)");
}

int	total_ops(t_stack *stack_a, t_stack *stack_b)
{
	int	total;

	total = 0;
	total += stack_a->px + stack_a->rr + stack_a->rrr;
	total += stack_a->rrx + stack_a->rx;
	total += stack_a->ss + stack_a->sx;
	total += stack_b->px + stack_b->rrx + stack_b->rx + stack_b->sx;
	return (total);
}

void	bench(t_stack *stack_a, t_stack *stack_b, t_config *conf, float order)
{
	ft_printf("[bench] disorder: %f%%\n", order * 100);
	if (conf->mod == 0)
		ft_printf("[bench] strategy: simple / O(n^2)\n");
	else if (conf->mod == 1)
		ft_printf("[bench] strategy: medium / O(n√n)\n");
	else if (conf->mod == 2)
		ft_printf("[bench] strategy: complex / O(nlogn)\n");
	else
		ft_printf("[bench] strategy: adaptive / O(%s)\n", check_mod(order));
	ft_printf("[bench] total_ops: %i\n", total_ops(stack_a, stack_b));
	ft_printf("[bench] sa: %i sb: %i ", stack_a->sx, stack_b->sx);
	ft_printf("ss: %i pa: %i pb: %i\n", stack_a->ss, stack_a->px, stack_b->px);
	ft_printf("[bench] ra: %i rb: %i ", stack_a->rx, stack_b->rx);
	ft_printf("rr: %i rra: %i ", stack_a->rr, stack_a->rrx);
	ft_printf("rrb: %i rrr: %i\n", stack_b->rrx, stack_a->rrr);
}
